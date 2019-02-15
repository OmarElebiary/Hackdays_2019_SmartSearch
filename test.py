# Loading the data files
import metrics
from files import get_filtered_data
from preprocessing import preprocess

rootDir = '../docs_txt'
print("Loading data...")
(file_data, file_dirs) = get_filtered_data(rootDir)
tokens_filtered = preprocess(file_data)


token2files, filentoken2occ, token2occ = metrics.get_counts(tokens_filtered)
filentoken2tfidf = metrics.get_tfidf(tokens_filtered, token2files, filentoken2occ)


print(filentoken2tfidf[212, 'zimmerlin'])
