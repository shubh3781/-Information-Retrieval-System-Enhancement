import sys, math

def parseArgument():
    if len(sys.argv) != 3:
        sys.exit("Errors in Arguments")
    return str(sys.argv[1]), str(sys.argv[2])

def readContent(infile):
    data = {}
    with open(infile, 'r', encoding = 'utf-8') as fs:
        for line in fs: 
            word = line.split()[0]
            data[word] = {}
            for docFreq in line.split()[1:]:
                document, count = docFreq.split('|')
                data[word][document] = int(count)
    return data

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

def writeContent(outFile, data):
    documents = list(data.keys())
    words = []
    for document in data:
        for word in data[document]:
            words.append(word)
    words = list(set(words))

    documents.sort()
    words.sort()
    
    fs = open(outFile, 'w')
    fs.write('\t' + "\t".join(documents) + '\n')
    for word in words:
        fs.write(word)
        for document in documents: 
            if document in data and word in data[document]: fs.write('\t' + str(data[document][word]))
            else: fs.write('\t0')
        fs.write('\n')
    fs.close()

if __name__ == "__main__":
    inFile, outFile = parseArgument()
    data = readContent(inFile)
    model, _ = genModel(data)
    writeContent(outFile, model)