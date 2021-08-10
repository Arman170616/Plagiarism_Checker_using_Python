# Plagiarism_Checker_using_Python
plagiarism Checker in text using Python


I am making a plagiarism checker using Python as a hobby project. The following steps are to be followed:

  1. Tokenize the document.

  2. Remove all the stop words using NLTK library.

  3. Use GenSim library and find the most relevant words, line by line. This can be done by creating the LDA or LSA of the document.

  4. Use Google Search API to search for those words.

Note: you might have chosen to use the Google API and search the whole document at once. This will work when you are working with smaller amount of data. However when building plagiarism checker for sites and webscraped data, we will need to apply NLTK algorithms.

The Google search API will result in the top articles which have the same words which were resulted in the LDA or LSA from GenSim library functions of Python.

Hope it helped.
