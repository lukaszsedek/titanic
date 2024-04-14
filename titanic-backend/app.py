from flask import Flask
from flask_cors import CORS, cross_origin
 
app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
 
 
@app.route("/")
@cross_origin()
def hello():
    return {
        "Status": "True"
    }