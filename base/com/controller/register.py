from base import app
import flask

app.route("/", METHODS=["GET", "POST"])
def welcome_page():
    return flask.render_template("welcomePage.html")