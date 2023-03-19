from flask import Flask
from flask import request
from flask import jsonify
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
  dsn = "http://c18b7042926d41feb1a67f19da0fee45@sentry.cauchy.link/3",
  integrations = [FlaskIntegration()],
  traces_sample_rate = 0.5
)

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "Hello, Kubernetes!\n"

@app.route("/echo", methods = ["POST"])
def echo():
  body = request.get_json()
  return jsonify(body)

@app.route("/error", methods = ["GET"])
def error():
  return 1 / 0