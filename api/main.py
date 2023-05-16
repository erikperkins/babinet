from flask import Flask
from flask import request
from flask import jsonify
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from sentry_sdk import capture_exception
from sentry_sdk import capture_message

sentry_sdk.init(
  dsn = "https://5e2ac15c66d64cfa97d13edcacd6e9ec@sentry.cauchy.link/2",
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

@app.route("/exception", methods = ["GET"])
def exception():
  value = 1 / 0
  return "Exception!"

@app.route("/error", methods = ["GET"])
def error():
  try:
    value = 1 / 0
  except Exception as e:
    capture_exception(e)
  return "Error!"

@app.route("/message", methods = ["GET"])
def message():
  capture_message('Hello, Sentry!')
  return 'Sent message'

@app.route("/api_error", methods = ["GET"])
def api_error():
  capture_message('API Error!')
  return 'API error!'