from collections import defaultdict

import metrics
from files import get_filtered_data
from preprocessing import preprocess


def search_query(query, filentoken2tfidf, token2files, debug=False):
    """

    :param query: Whole query (can be composed of multiple tokens)
    :param filentoken2tfidf:
    :return: Combined result of all tokens with (score, file index)
    """
    query_prep = preprocess([query])[0]
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
        weight = filentoken2tfidf[file, token]
        # weight = 1
        file_scores.append((file, weight))

    return file_scores


