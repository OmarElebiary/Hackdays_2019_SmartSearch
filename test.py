# Loading the data files
import metrics
from files import get_filtered_data
from preprocessing import preprocess
from search import search_query


def unit_test(rootDir):
    ''''''
    (file_data, file_dirs) = get_filtered_data(rootDir)
    tokens_filtered = preprocess(file_data)

    token2files, filentoken2occ, token2occ = metrics.get_counts(tokens_filtered)
    filentoken2tfidf = metrics.get_tfidf(tokens_filtered, token2files, filentoken2occ)

    print('Loading done.')
    
    results = search_query('Artech c32-hp1 atex', filentoken2tfidf, debug=True)
    resultsDirs = [(score, file_dirs[idx], debug) for score, idx, debug in results]

    print(resultsDirs)

    print('Done.')


def main():
    rootDir = '../docs_txt'