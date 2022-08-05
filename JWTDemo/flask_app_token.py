from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
import jwt
import uuid
from datetime import  *
import  json

from functools import wraps
app = Flask(__name__)
'''
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

class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(1000))
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    user_id = db.Column(db.Integer, primary_key=True) ## id of User tabel


def encodeJwtToken():
    exp = datetime.now(tz=timezone.utc) + timedelta(seconds=30)
    iss = {"iss": "urn:foo"}
    iat = {"iat": datetime.now(tz=timezone.utc)}
    sub = {'sub': '25c37522-f148-4cbf-8ee6-c4a9718dd0af'}
    aud = {"aud": ["urn:foo", "urn:bar"]}
    payload = {"iss": "urn:foo", "iat": datetime.now(tz=timezone.utc),
               'sub': '25c37522-f148-4cbf-8ee6-c4a9718dd0af',
               "aud": ["urn:foo", "urn:bar"], "exp":  datetime.now(tz=timezone.utc) + timedelta(days=30)}

    encoded = jwt.encode(payload, "secret", algorithm="HS256")
    return encoded

def decodeJWToken(token):
    decoded = jwt.decode(token, "secret", options={"verify_signature": True, "verify_aud": False}, algorithms=["HS256"])
    #decoded = jwt.decode(token, "secret", audience="urn:foo", algorithms=["HS256"])
    return decoded


def validate_user(username, passssword):
    flag = False
    user = User.query.filter_by(api_username=username, api_password=passssword, is_active=1).first()
    if user:
        flag = True
    return flag


@app.route("/token", methods = ["POST"])
def token():
   print("calling token API")
   if request and request.is_json:
       json_data = request.json
       try:
           api_username = json_data.get('username')
           api_password = json_data.get('password')
           if api_password and api_password:
                """Calling db services"""
                if validate_user(api_username, api_password):
                    resp = {"token": encodeJwtToken()}
                    return jsonify(resp)
                else:
                    return jsonify({"error": "Username or password is Invalid"})
           else:
               return jsonify({"error": "Username or password is empty"})
       except:
           return jsonify({"error": "Invalid Request"})

   return jsonify({"error": "Invalid Request"})


@app.route("/test")
def test():
    if request:
        try:
            token = request.headers['token']
            if token:
               payload = decodeJWToken(token)
               print(payload)
               return jsonify({"status": "success"})
            else:
                return jsonify({"error": "token empty"})
        except:
            return jsonify({"error": "Missing token header"})
    else:
        return jsonify({"error": "Invalid Request"})




if __name__ == "__main__":
    db.create_all()
    user = User(
        public_id=str(uuid.uuid4()),
        name="ravi",
        email="ravi@gmail.com",
        api_password="ravi",
        api_username="ravi"
    )
    # insert user
    db.session.add(user)
    db.session.commit()
    app.run(port=5001, host="0.0.0.0", debug=False)