from collections import defaultdict

import metrics
from files import get_filtered_data
from preprocessing import preprocess

rootDir = '../docs_txt'
(data, fileDirs) = get_filtered_data(rootDir)
tokens_filtered = preprocess(data)

token2files, filentoken2occ, token2occ = metrics.get_counts(tokens_filtered)
filentoken2tfidf = metrics.get_tfidf(tokens_filtered, token2files, filentoken2occ)

print('Loading done.')



def search(query, filentoken2tfidf, debug=False):
    """

    :param query: Whole query (can be composed of multiple tokens)
    :param filentoken2tfidf:
    :return: Combined result of all tokens with (score, file index)
    """
    query_prep = preprocess([query])[0]
    if debug:
        print('"{}" -> {}'.format(query, query_prep))
    T = len(query_prep)
    scores = []
    # accumulate results for individual tokens
    for i in range(T):
        scores.append(search_token(query_prep[i], filentoken2tfidf, token2files))

    # combine results
    file2totalscore = defaultdict(float)
    if debug:
        file2totalscore_debug = defaultdict(str)
    for i in range(T):
        for file, score in scores[i]:
            file2totalscore[file] += score
            if debug:
                file2totalscore_debug[file] += ' + ({}, {:.5f})'.format(query_prep[i], score)

    # sort by score
    scorefile = []
    for file, total_score in file2totalscore.items():
        if debug:
            scorefile.append((total_score, file, file2totalscore_debug[file][3:]))
        else:
            scorefile.append((total_score, file))
    scorefile = sorted(scorefile)[::-1]

    return scorefile



def search_token(token, filentoken2tfidf, token2files):
    """

    :param token: single token
    :param filentoken2tfidf:
    :param token2files:
    :return: Result of this single token
    """

    file_scores = []
    for file in token2files[token]:
        file_scores.append((file, filentoken2tfidf[file, token]))

    return file_scores


results = search('Artech c32 hp1 atex', filentoken2tfidf, debug=True)
resultsDirs = [(score, fileDirs[idx], debug) for score, idx, debug in results]

print('Done.')