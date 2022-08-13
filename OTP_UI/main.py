from flask import *
from flask_sqlalchemy import SQLAlchemy
from datetime import  *

app = Flask(__name__)
'''
SQLLight Studio
# configuration
# NEVER HARDCODE YOUR CONFIGURATION IN YOUR CODE
# INSTEAD CREATE A .env FILE AND STORE IN IT
'''
app.config['SECRET_KEY'] = 'ravi'
# database name
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# creates SQLALCHEMY object
db = SQLAlchemy(app)

# Database ORMs
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    public_id = db.Column(db.String(50), unique = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(70), unique = True)
    api_username = db.Column(db.String(50), unique = True)
    api_password = db.Column(db.String(80))
    is_active = db.Column(db.Integer, default=1) ## 1- means active and 0 means deactivate
    created_date =db.Column(db.DateTime, nullable=False, default=datetime.now())
    last_modified_date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    #default=datetime.strftime(datetime.now(), "%b %d %Y"))


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/demo")
def demo():
    return render_template("demo.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/feedback")
def feedback():
    return render_template("feedback.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["username"] and request.form["password"]:
            username = request.form["username"]
            password = request.form["password"]
            # status = validate_user(username, password)
            status = True
            if status:
                return redirect(url_for("welcome"))
            else:
                message = "Plz check username and password"
                return render_template("login.html", result=message)
        else:
            message = "Plz check username and password"
            return render_template("login.html", result=message)
    return render_template("login.html")


@app.route("/signup_submit", methods=["POST"])
def signup_submit():
    if request.method == "POST":
        if request.form:
            first_name = request.form["first_name"]
            last_name = request.form["last_name"]
            email = request.form["email"]
            mobile_no = request.form["mobile_no"]
            dob = request.form["dob"]
            city = request.form["city"]
            country = request.form["country"]
            # registered_details(first_name, last_name, email, mobile_no,dob, city, country)
            message = "You have registered successfully"
            return render_template("signup.html", result=message)
        else:
            message = "Plz enter correct details"
            return render_template("signup.html", result=message)
    return render_template("signup.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5002", debug=True)