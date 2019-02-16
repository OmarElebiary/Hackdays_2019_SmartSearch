import sys

import preprocessing


def preprocess_synonym_list(path_in, path_out):
    synlist = []
    with open(path_in) as f:
        for l in f.read().split('\n'):
            syns = list(l.split())
            synlist.append(syns)

    tokens_filtered_all = []
    for syn in synlist:
        tokens = preprocessing._tokenize(syn)
        tokens_filtered = []
        # add with and without stemming
        for t in tokens:
            tokens_filtered.append(preprocessing._remove_stopwords(t))
        tokens_filtered_all.append(tokens_filtered)

    with open(path_out, 'w') as f:
        for t in tokens_filtered_all:
            f.write(' '.join(map(lambda x: x[0], filter(None, t))) + '\n')


def read_synms_list():
    synlist = []
    with open('synonyms_german_prepr.txt') as f:
        for l in f.read().split('\n'):
            syns = list(l.split())
            synlist.append(syns)
    syn_dict={}
    for d in filter(None, synlist):
        #print (d)
        for i,j in enumerate(d):
            if i>0:
                syn_dict.update({d[i]:d[0]})

    #print (syn_dict)
    return syn_dict

def preprocess_wordlist(path_in, path_out):
    with open(path_in) as f:
        wordlist = f.read().split('\n')

    tokens = preprocessing._tokenize(wordlist)
    tokens_filtered = []
    for t in tokens:
        tokens_filtered.append(preprocessing._remove_stopwords(t))
        tokens_filtered.append(t)

    with open(path_out, 'w') as f:
        f.write('\n'.join(map(lambda x: x[0], filter(None, tokens_filtered))))

if __name__ == '__main__':
    preprocess_synonym_list('synonyms_german.txt', 'synonyms_german_prepr.txt')
    preprocess_wordlist('wordlist_german.txt', 'wordlist_german_prepr.txt')