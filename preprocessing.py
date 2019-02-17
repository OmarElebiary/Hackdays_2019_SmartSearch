import re
import preprocess_files
from nltk.stem.snowball import GermanStemmer


gs = GermanStemmer()
punctuations = '''!()-[]{};:'"\,<>/?@#$%^&*_~'''



def match_synms(tokens):
    syn_dict = preprocess_files.read_synms_list()
    for t in tokens:
        for (idx, val) in enumerate(t):
            if val in syn_dict:
                t[idx] = syn_dict[val]

    return tokens

def _remove_punctuation(tokens):
    tokens_filt = []
    for gT in tokens:
        if gT not in punctuations: tokens_filt.append(gT)
    return tokens_filt


def _remove_stopwords(tokens):
    '''Remove stop words from an array of tokens'''

    stopWords = ['the', 'to', '-', 'pr', 'der', 'is', 'of', 'die', 'in', 'and', 'und', '–', '•', '✔', '●', 'a']

    tokens_filt = []
    for gT in tokens:
        if gT not in stopWords: tokens_filt.append(gT)

    #punctuations_filtered_tokens = _remove_punctuation(tokens_filt)

    return tokens_filt #[gs.stem(word).strip() for word in tokens_filt]


def _tokenize(data):
    '''Extract different token arrays for every single files in data (>>tokens)
    and extract ONE single token array for all files (>>globalTokens)'''
    tokens = []
    for d in data:
        d = d.lower()
        tokenized = re.split(r'\W', d)
        # remove empty strings
        tokenized = list(filter(None, tokenized))
        tokens.append(tokenized)
    return tokens

def preprocess(data):
    """

    :param data: list of lists
    :return: list of lists with tokens
    """
    tokens = _tokenize(data)
    tokens_filtered = []
    for t in tokens:
        tokens_filtered.append(_remove_stopwords(t))

    # tokens_filtered_syn = match_synms(tokens_filtered)
    return tokens_filtered