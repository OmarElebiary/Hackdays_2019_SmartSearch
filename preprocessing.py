import re
from nltk.stem.snowball import GermanStemmer
gs = GermanStemmer()
punctuations = '''!()-[]{};:'"\,<>/?@#$%^&*_~'''


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

    return [gs.stem(word).strip() for word in tokens_filt]


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

def preprocess(data, dictionary):
    """

    :param data: list of strings
    :return: list of lists with tokens
    """
    tokens = _tokenize(data)
    tokens_filtered = []
    for t in tokens:
        tokens_filtered.append(_remove_stopwords(t))

    segmented = []
    for outer in tokens:
        segmented.append([])
        for inner in outer:
            segmented[-1].extend(segment(inner, dictionary))

    return segmented


def segment(token, dictionary):
    """
    Segments single token into multiple ones for compound nouns
    (e.g. werkstoff -> werk stoff)
    :param token:
    :return:
    """
    n = len(token)
    segments = []
    start = 0
    min_segment_len = 15
    for i in range(len(token)):
        if i - start >= min_segment_len - 1 and n - (i + 1) >= min_segment_len and token[start:i + 1] in dictionary:
            segments.append(token[start:i + 1])
            start = i + 1

    # add remaining str
    segments.append(token[start:])

    return segments
