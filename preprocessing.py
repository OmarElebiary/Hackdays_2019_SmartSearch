import re


def _remove_stopwords(tokens):
    '''Remove stop words from an array of tokens'''

    # nltk.download('stopwords')
    # stopWords = set(stopwords.words('english'))
    stopWords = ['the', 'to', '-', 'pr', 'der', 'is', 'of', 'die', 'in', 'and', 'und', '–', '•', '✔', '●', 'a']

    tokens_filt = []
    for gT in tokens:
        if gT not in stopWords: tokens_filt.append(gT)

    return tokens_filt


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

    return tokens_filtered