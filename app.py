from flask import Flask
from flask import render_template

app = Flask(__name__)

slack_app = App(process_before_response=True)

handler = SlackRequestHandler(app)

@app.route("/")
def hello_world():
    return render_template("index.html")
