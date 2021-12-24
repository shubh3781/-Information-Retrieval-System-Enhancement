
def parseArgument():
    #hrFile = input("ENter the filename of historical results: ")
    #seg = int(input("Enter the segments: "))
    #liveFile = input("Enter the filename of live results: ")
    #fus = input("Enter models (comma seperated) which you want to fuse out of (A,B,C,D): ").split(',')
    
    hrFile = 'hresult_9d29b608b86d50941b3e2136ffbb375c.csv'
    seg = 10
    liveFile = 'liveresult_e59ed48679c86693181f010e49a0fc2b.csv'
    fus = 'A,B,C,D'
    
    return hrFile, liveFile, seg, fus.split(',')

def readContent(hrFile, liveFile):
    hrData = {}
    with open(hrFile, 'r', encoding = 'utf-8', errors = 'ignore') as file:
        lines = file.read().split('\n')
        for i in range(len(lines)-1):
            line = lines[i].strip().split(',')
            if i == 0: hrData[line[0][1:]] = line[1:]
            else: hrData[line[0]] = line[1:]
        
    liveData, documents = {}, []
    with open(liveFile, 'r', encoding = 'utf-8', errors = 'ignore') as file:
        lines = file.read().split('\n')
        for i in range(len(lines)-1):
            line = lines[i].strip().split(',')
            documents += line[1:]
            if i == 0: liveData[line[0][1:]] = line[1:]
            else: liveData[line[0]] = line[1:]

    return hrData, liveData, list(set(documents))

def genHelpingModel(hrData, liveData, seg):
    model, docSeg, num_queries = {}, {}, {}
    for key in hrData:
        if key[0] in num_queries: num_queries[key[0]] += 1
        if key[0] not in num_queries: num_queries[key[0]] = 1
    
    for m in hrData.keys():
        mod = m[0]
        model[m], seg_len = {}, []
        
        seg_len = [ len(hrData[m])//seg ]*seg
        for i in range(seg):
            if i < len(hrData[m])%seg: seg_len[i] += 1
            
        key = 1
        if mod not in docSeg.keys(): docSeg[mod] = {}
        for i in range(len(hrData[m])):
            if key in model[m]:
                if len(model[m][key]) == seg_len[key-1]: 
                    key += 1

            if key not in model[m]: 
                model[m][key] = {}

            docSeg[mod][liveData[mod][i]] = key
            model[m][key][liveData[mod][i]] = hrData[m][i]
    return model, docSeg, num_queries

def genModel(model, docSeg, num_queries):
    prob = {}
    for m in model.keys():
        mod = m[0]
        if mod in prob: pass
        else: prob[mod] = {}

        for key in model[m]:
            prob[mod][key] = 0
            
    for m in model:
        for key in model[m]: prob[m[0]][key] += sum( value == 'R' for value in model[m][key].values()) /len(model[m][key])
            
    for mod in prob.keys(): prob[mod] = { k: v / num_queries[mod] for k, v in prob[mod].items()}
        
    
    return prob

def fusion(prob, docSeg, fus, documents):
    result = {}
    for mod in fus:
        i = 0
        while i < len(documents):
            if documents[i] not in docSeg[mod].keys(): p = 0 
            else: p = prob[mod][docSeg[mod][documents[i]]]/docSeg[mod][documents[i]]
            
            if documents[i] in result.keys(): result[documents[i]] += p
            else: result[documents[i]] = p

            i += 1
                
    fusion = sorted(result, key=result.get, reverse=True)
    fs = open('output.txt', 'w')
    for f in fusion:
        fs.write(str(f) + '\n')


if __name__ == "__main__":
    hrFile, liveFile, seg, fus = parseArgument()
    hrData, liveData, documents = readContent(hrFile, liveFile)
    model, docSeg, num_queries = genHelpingModel(hrData, liveData, seg)
    prob = genModel(model, docSeg, num_queries)
    fusion(prob, docSeg, fus, documents)