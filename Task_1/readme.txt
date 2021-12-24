Python 3.6.9 and nltk is required for the scripts,
 - preprocessing.py
 - inverted_index.py
 - TF_IDF.py
 - cosine_similarity.py
 - IR.py 

How to run the code:
    1. pip install nltk (if it is not installed)

    2. python3 preprocessing.py infolder outfolder stopwords.txt

       Expected Input and Output file of 2 has been attached with the project as stopwords.txt.

    3. python3 inverted_index.py outfolder invOut.txt

       Expected Input and Output file of 3 has been attached with the project as invOut.txt.

    4. python3 TF_IDF.py invOut.txt tfidfOut.txt

       Expected Input and Output file of 4 has been attached with the project as tfidfOut.txt.

    5. python3 cosine_similarity.py tfidfOut.txt D2 D1

       Console Output of 5 
       Console Output of cosine_similarity.py: 
       similarity:  0.5352529324140219   

6. python3 IR.py infolder "Second Sample" stopwords.txt

   Console Output of IR.py: 
            D2:     0.687277874335952
            D1:     0.49645834945572076
            D3:     0.0

