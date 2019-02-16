from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
from flask import jsonify
from flask import send_file
from fileFinder import search_files

from collections import defaultdict
import sys
import os
sys.path.append("../../../.")
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import metrics
from files import get_filtered_data, get_real_filepath
from preprocessing import preprocess
from search import search_query

app = Flask(__name__, static_url_path='/assets')
cors = CORS(app)

@app.route('/', methods=['POST'])
@cross_origin()
def search():
    searchTerm = request.data
    # Perform the search query
    # Execute the searching script

    results = search_query(searchTerm.decode('utf-8'), filentoken2tfidf, token2files)

    n_results = 5
    paths = [get_real_filepath(rootDir, realFileDir, file_dirs, i) for i in range(n_results)]
    print(paths)

    return jsonify(paths)

@app.route('/file/<name>')
def static_file(name):
    filePath, fileExtension = search_files('Marking Map & Mill Test Report SN 3268.pdf')
    print(filePath)
    return send_file(filePath)

if __name__ == '__main__':

    rootDir = "../../../../docs_txt"
    realFileDir = "../../../classified documents"

    (file_data, file_dirs) = get_filtered_data(rootDir)
    tokens_filtered = preprocess(file_data)

    token2files, filentoken2occ, token2occ = metrics.get_counts(tokens_filtered)
    filentoken2tfidf = metrics.get_tfidf(tokens_filtered, token2files, filentoken2occ)

    app.run(debug=True)
