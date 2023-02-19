from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "Hello, Docker!\n"

@app.route("/echo", methods = ["POST"])
def echo():
  body = request.get_json()
  return jsonify(body)
