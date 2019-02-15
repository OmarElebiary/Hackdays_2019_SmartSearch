import nltk


def _remove_stopwords(tokens):
    '''Remove stop words from an array of tokens'''

    from nltk.corpus import stopwords
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
        tokens.append(nltk.word_tokenize(d.lower()))
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