from flask import Flask
from flask import request
from flask import jsonify
import os
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from sentry_sdk import capture_exception
from sentry_sdk import capture_message
from .thread import TripThread

sentry_sdk.init(
  dsn = "https://c18b7042926d41feb1a67f19da0fee45@sentry.cauchy.link/3",
  integrations = [FlaskIntegration()],
  traces_sample_rate = 0.5
)

app = Flask(__name__)

trips = TripThread(
  minio_access_key = os.environ.get('MINIO_ACCESS_KEY'),
  minio_secret_key = os.environ.get('MINIO_SECRET_KEY')
)

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

@app.route("/start", methods = ["GET"])
def start_trips():
  trips.start()
  return "Started\n"

@app.route("/stop", methods = ["GET"])
def stop_trips():
  trips.stop()
  return "Stopped\n"