import sys
from os import listdir
from os.path import isfile, join

def parseArgument():
    if len(sys.argv) != 3:
        sys.exit("Errors in Arguments")
    return str(sys.argv[1]), str(sys.argv[2])

def readContent(infolder):
    data = {}
    files = [f for f in listdir(inFolder) if isfile(join(inFolder, f))]

    for file in files:
        data[file] = []
        with open(infolder + '/' + file, 'r', encoding = 'utf-8') as fs:
            for line in fs: data[line.strip().split()[0]] += line.strip().split()[1:]    
    return data

def genInv(data):
    dic = {}
    for document in data.keys():
        for word in data[document]:
            if word in dic.keys():
                if document in dic[word]: dic[word][document] += 1
                else: dic[word][document] = 1
            else: dic[word] = {document : 1}
    return dic

def writeContent(outFile, data):
    fs = open(outFile, 'w')
    for word in data:
        fs.write(word)
        for document in data[word]: fs.write('\t' + document + '|' + str(data[word][document]))
        fs.write('\n')
    fs.close()

if __name__ == "__main__":
    inFolder, outFile = parseArgument()
    data = readContent(inFolder)
    data = genInv(data)
    writeContent(outFile, data)