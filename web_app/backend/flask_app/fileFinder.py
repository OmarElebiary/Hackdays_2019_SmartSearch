import os
import sys

def search_files(name):
    for root, dirs, files in os.walk('assets/classified documents'):
        for file in files:
            fileName, fileExtension = os.path.splitext(file)
            if file == name:
                filePath = root + '/' + file
                return filePath, fileExtension
