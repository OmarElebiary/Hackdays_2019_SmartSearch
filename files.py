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
            dataFiltered.append(fileData)
            filesFiltered.append(allFiles[ind])

    return (dataFiltered, filesFiltered)


def get_filename(query_results, file_dirs, N=5):
    '''
    '''
    return [file_dirs[query_results[i][1]] for i in range(N)]


def get_real_filepath(rootDir, realFileDir, file_dirs, fileIndex):
    fileName = file_dirs[fileIndex].replace(rootDir, realFileDir)
    return fileName[:-4]


def get_dictionary():
    with open('wordlist_german_prepr.txt') as f:
        return set(f.read().split('\n'))
