from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
from flask import jsonify

app = Flask(__name__)
cors = CORS(app)

@app.route('/', methods=['POST'])
@cross_origin()
def search():
    searchTerm = request.data
    # Perform the search query
    # Execute the searching script
    return searchTerm

if __name__ == '__main__':
    app.run(debug=True)