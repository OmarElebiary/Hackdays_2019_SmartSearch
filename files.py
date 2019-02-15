import os
import string

import nltk


def get_filtered_data(rootDir):
    ''' Return filtered data from root folder as array of strings and
    the corresponding paths to the respective files
    '''
    allDirs = []
    allFiles = []
    files_txt = []
    data = []
    dataFiltered = []
    filesFiltered = []

    translator = str.maketrans('', '', string.punctuation)

    for root, dirs, files in os.walk(rootDir, topdown=False):
        for name in dirs:
            allDirs.append(os.path.join(root, name))

    for dP in allDirs:
        onlyFiles = [f for f in os.listdir(dP) if os.path.isfile(os.path.join(dP, f))]
        for oF in onlyFiles: allFiles.append(os.path.join(dP, oF))

    for aF in allFiles:
        # with open(aF, 'r', encoding = "ISO-8859-1") as newFile:
        with open(aF, 'r', encoding="utf-8", errors='replace') as newFile:
            data.append(newFile.read())

    for ind, fileData in enumerate(data):
        filt = [d == '\x0c' for d in fileData]
        if sum(filt) < len(filt):
            s = fileData.lower()
            s = s.translate(translator)
            dataFiltered.append(s)
            filesFiltered.append(allFiles[ind])

    return (dataFiltered, filesFiltered)


def document_to_words(doc):
    doc = doc.split('\n')
    doc_short = []
    doc_words = []
    doc_words_short = []
    for d in doc:
        if len(d) > 1: doc_short.append(d)
    for d in doc_short:
        doc_words += d.split(' ')
    for d in doc_words:
        if len(d) > 1: doc_words_short.append(d)
    return doc_words_short


def remove_stopwords(tokens):
    '''Remove stop words from an array of tokens'''

    from nltk.corpus import stopwords
    # nltk.download('stopwords')
    # stopWords = set(stopwords.words('english'))
    stopWords = ['the', 'to', '-', 'pr', 'der', 'is', 'of', 'die', 'in', 'and', 'und', '–', '•', '✔', '●', 'a']

    tokens_filt = []
    for gT in tokens:
        if gT not in stopWords: tokens_filt.append(gT)

    return tokens_filt


def tokenize(data):
    '''Extract different token arrays for every single files in data (>>tokens)
    and extract ONE single token array for all files (>>globalTokens)'''
    tokens = []
    for d in data:
        tokens.append(nltk.word_tokenize(d))
    return tokens
