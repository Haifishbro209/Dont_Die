from flask import *
from sqlalchemy import *
from database import *

app = Flask(__name__)

@app.route("/")
def index():
    
    return render_template("landingpage.html")

@app.route("/health/<username>")
def sign_up(username):
    return render_template("health.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/app/<user_name>")
def overview(user_name):
    add_user(user_name)
    return render_template("app.html")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)