Project Summary: Information Retrieval System Enhancement
Overview
This project aims to develop and enhance an Information Retrieval (IR) system using various Python scripts and methodologies. It is divided into two main tasks, each focusing on distinct aspects of IR—ranging from preprocessing and indexing to advanced data fusion techniques for result optimization.

Task 1: Building the IR System
Objective: Implement the foundational components of an IR system, including text preprocessing, inverted indexing, TF-IDF scoring, and similarity calculations.

Preprocessing: Utilizes preprocessing.py to clean text data by tokenization, normalization, and removing stopwords listed in stopwords.txt.
Inverted Index: inverted_index.py generates an inverted index, mapping terms to their document locations, facilitating efficient search queries.
TF-IDF Calculation: TF_IDF.py calculates Term Frequency-Inverse Document Frequency scores to evaluate word importance within documents, assisting in ranking search results.
Cosine Similarity: Implements cosine_similarity.py to compute similarity scores between documents, aiding in identifying relevant documents to user queries.
IR System Interface: IR.py serves as the query interface, allowing users to search the corpus and receive ranked results based on relevance.
Task 2: Enhancing the IR System with Data Fusion
Objective: Enhance the retrieval effectiveness of the IR system through the application of data fusion techniques, specifically using the ProbFuse algorithm.

Data Fusion: Utilizes probfuse.py to implement the ProbFuse algorithm, combining results from multiple retrieval systems to improve overall search performance.
Result Analysis: Processes result files (e.g., hresult_9d29b608b86d50941b3e2136ffbb375c.csv, liveresult_e59ed48679c86693181f010e49a0fc2b.csv) and analyzes the fused rankings in output.txt, showcasing the optimized order of document relevance.
Implementation and Usage
The project is developed in Python 3.6.9, requiring the NLTK library for natural language processing tasks. The readme.txt file provides detailed instructions on installing dependencies, running each script, and processing the data for both tasks. Users can follow these steps to set up the IR system, perform searches, and evaluate the enhancements provided by data fusion.

Conclusion
This project demonstrates the application of foundational IR techniques and advanced data fusion algorithms to create a more effective and efficient information retrieval system. By systematically addressing each component—from preprocessing to probabilistic fusion—the project showcases a comprehensive approach to improving search relevance and performance in a corpus of documents.

