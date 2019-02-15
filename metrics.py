from collections import defaultdict
import math


def get_counts(tokens_filtered):
    token2files = defaultdict(set)
    filentoken2occ = defaultdict(int)
    token2occ = defaultdict(int)
    for i, tokens in enumerate(tokens_filtered):
        for t in tokens:
            if i not in token2files[t]:
                token2files[t].add(i)
            filentoken2occ[i, t] += 1
            token2occ[t] += 1

    return token2files, filentoken2occ, token2occ


def get_tfidf(tokens_filtered, token2files, filentoken2occ):
    n_docs = len(tokens_filtered)
    idf = {}
    for token, files in token2files.items():
        token_file_n = len(files)
        idf_token = math.log(n_docs / token_file_n)
        idf[token] = idf_token

    filentoken2tfidf = defaultdict(int)
    for file, token in filentoken2occ.keys():
        doc_len = len(tokens_filtered[file])
        token_occ_doc = filentoken2occ[file, token]
        filentoken2tfidf[file, token] = token_occ_doc / doc_len * idf[token]

    return filentoken2tfidf