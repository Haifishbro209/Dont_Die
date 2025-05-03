from flask import *
from sqlalchemy import *
from database import *

app = Flask(__name__)

@app.route("/api/login",methods=['GET', 'POST'])
def login_api():
    if request.method == 'POST':
        email = request.form['email']
        add_user(email)
        return redirect(url_for('overview',user_name = email))
    else:
        return redirect(url_for("login"))  

@app.route("/api/risks/<username>/")
def user_risks(username):
    with open("risks.json") as f:
        all_risks = json.load(f)["risks"]

    #smart algo

    user_specific_ids = ["low_sleep", "high_bp"]  
    selected_risks = [r for r in all_risks if r["id"] in user_specific_ids]

    return jsonify(selected_risks)

@app.route("/")
def index():
    return render_template("landingpage.html")

@app.route("/health/<username>")
def sign_up(username):
    return render_template("health.html")


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/sources")
def sources():
    return render_template("sources.html")

@app.route("/app/<user_name>")
def overview(user_name):
    add_user(user_name)
    return render_template("app.html")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)