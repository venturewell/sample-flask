from flask import Flask
import logging
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler

logging.basicConfig(level=logging.DEBUG)
app = App()

@app.middleware  # or app.use(log_request)
def log_request(logger, body, next):
    logger.debug(body)
    return next()

@app.event("app_mention")
def event_test(body, say, logger):
    logger.info(body)
    say("What's up?")

@app.event("message")
def handle_message():
    pass

from flask import Flask, request

flask_app = Flask(__name__)
handler = SlackRequestHandler(app)

@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)

