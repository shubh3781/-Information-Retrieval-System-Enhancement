import sys, math
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
    return data, stops

def genInv(data):
    dic = {}
    for document in data.keys():
        for word in data[document].split():
            if word in dic.keys():
                if document in dic[word]: dic[word][document] += 1
                else: dic[word][document] = 1
            else: dic[word] = {document : 1}
    return dic

def genModel(data):
    model = {}
    for word in data: 
        for document in data[word]:
            if document not in model: model[document] = {}
            model[document][word] = data[word][document]

    idf = {}
    for word in data:
        idf[word] = 1+math.log(len(model)/len(data[word]))

    for document in model:
        for word in model[document]:
            model[document][word] = model[document][word]/max(model[document].values())
            model[document][word] = model[document][word]*idf[word]

    return model, idf

def calCos(tfidf, idf, query):
    model = {}

    documents = list(tfidf.keys())
    words = []
    for document in tfidf:
        for word in tfidf[document]:
            words.append(word)
    words = list(set(words))

    documents.sort()
    words.sort()

    for document in documents:
        model[document] = []
        for word in words: 
            if word in tfidf[document]: model[document].append(tfidf[document][word])
            else: model[document].append(0)

    queryVec = [0]*len(words)
    for token in query.split(): 
        if token in words: queryVec[words.index(token)] = 1

    for i in range(len(words)):
        queryVec[i] *= idf[words[i]]

    sim = {}
    for document in documents:
        sumxx = sum([x*y for x,y in zip(queryVec, queryVec)])
        sumyy = sum([x*y for x,y in zip(model[document], model[document])])
        sumxy = sum([x*y for x,y in zip(queryVec, model[document])])
        
        cosine=0
        if sumxx*sumyy != 0: cosine = sumxy/math.sqrt(sumxx*sumyy)
        sim[document] = cosine

    sim = {k: v for k, v in sorted(sim.items(), key=lambda item: item[1], reverse=True)}
    for document in sim: print(document + ":\t" + str(sim[document]))

if __name__ == "__main__":
    inFolder, query, stopwordFile = parseArgument()
    data, stops = readContent(inFolder, stopwordFile)
    data, stops = preProces(data, stops)
    data = genInv(data)
    model, idf = genModel(data)

    query, stops = preProces({'query':query.split()}, stops)
    calCos(model, idf, query['query'])