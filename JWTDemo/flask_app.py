from flask import Flask, jsonify, request
import jwt
from datetime import  *
import  json
app = Flask(__name__)


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

@app.route("/token", methods = ["GET"])
def token():
   print("calling token API")
   resp =  { "token": encodeJwtToken()}
   return  jsonify(resp)

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
    app.run(port=5001, host="0.0.0.0", debug=False)