# Word Similarity
A system based on the principles of Language model and Continuous Bag of Words (CBOW) to determine the similarity between 2 words from the given corpus is built. We then evaluate the performance by comparing this with the scores produced by word2vec.

----------------
	FILES
----------------

* Similarity.py
  This file contains the main logic for our implementation. Needs to be run as python similarity.py
 
* sentence2vec 
  It is a folder which contains the word2vec module. It should be present in the same location as similarity.py

* TweetCleaner.py
  It is the pre-processing module which is used to clean to initial corpus. This file should also be present in the 
  same location as similarity.py

Note: The implementation given is a generic module to find the triplet count for all words, and not only for the words presented in our analysis document.