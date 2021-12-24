import sys, math

def parseArgument():
    if len(sys.argv) != 4:
        sys.exit("Errors in Arguments")
    return str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3])

def readContent(infile):
    data = {}
    with open(infile, 'r', encoding = 'utf-8') as fs:
        content = fs.read()
        lines = content.split('\n')
        documents = lines[0].split()
        for i in range(1, len(lines)):
            content = lines[i].split()
            if(len(content) > 0):
                data[content[0]] = []
                for j in range(1, len(content)): data[content[0]].append(float(content[j]))
    return data, documents

def genModel(data, documents):
    words = list(data.keys())
    model = {}
    for i in range(len(documents)):
        model[documents[i]] = []
        for word in words: model[documents[i]].append(data[word][i])

    return model

def calCos(model, docOne, docTwo):
    
    sumxx = sum([x*y for x,y in zip(model[docOne], model[docOne])])
    sumyy = sum([x*y for x,y in zip(model[docTwo], model[docTwo])])
    sumxy = sum([x*y for x,y in zip(model[docOne], model[docTwo])])
        
    cosine=0
    if sumxx*sumyy != 0: cosine = sumxy/math.sqrt(sumxx*sumyy)
    print("similarity: ", cosine)

if __name__ == "__main__":
    inFile, docOne, docTwo = parseArgument()
    data, documents = readContent(inFile)
    model = genModel(data, documents)
    calCos(model, docOne, docTwo)