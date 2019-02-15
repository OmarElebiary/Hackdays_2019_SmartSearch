# Loading the data files
import metrics
from files import get_filtered_data, tokenize, remove_stopwords

rootDir = '../docs_txt'
print("Loading data...")
(data, fileDirs) = get_filtered_data(rootDir)
print("Tokenizing...")
tokens = tokenize(data)
print("Removing stopwords...")
tokens_filtered = []
for t in tokens:
    tokens_filtered.append(remove_stopwords(t))


token2files, filentoken2occ, token2occ = metrics.get_counts(tokens_filtered)
filentoken2tfidf = metrics.get_tfidf(tokens_filtered, token2files, filentoken2occ)


print(filentoken2tfidf[212, 'zimmerlin'])
