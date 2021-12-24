import sys
from os import listdir
from os.path import isfile, join
from nltk.stem import PorterStemmer

def parseArgument():
    if len(sys.argv) != 4:
        sys.exit("Errors in Arguments")
    return str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3])

def readContent(infolder, stopwordFile):
    data = {}
    files = [f for f in listdir(infolder) if isfile(join(infolder, f))]

    for file in files:
        data[file] = []
        with open(infolder + '/' + file, 'r', encoding = 'utf-8') as fs:
            for line in fs:
                data[file] += line.strip().split()
    
    stops = []
    with open(stopwordFile, 'r', encoding = 'utf-8') as fs:
        stops = [ line.rstrip('\n') for line in fs ]

    return data, stops

def preProces(data, stops):
    stemmer = PorterStemmer()
    for i in range(len(stops)): stops[i] = stops[i].lower()

    for document in data:
        result = ''
        for i in range(len(data[document])):
            content = ''
            for character in data[document][i]:
                if character.isalpha(): content += character
            data[document][i] = content.lower()

        for token in data[document]:
            if token not in stops: result += stemmer.stem(token) + ' '
        
        data[document] = result[:len(result)-1]
    return data

def writeContent(outFolder, data):
    files = list(data.keys())
    for file in files:
        with open(outFolder + '/' + file, 'w') as fs:
            fs.write(file + '\t' + data[file])

if __name__ == "__main__":
    inFolder, outFolder, stopwordFile = parseArgument()
    data, stops = readContent(inFolder, stopwordFile)
    data = preProces(data, stops)
    writeContent(outFolder, data)