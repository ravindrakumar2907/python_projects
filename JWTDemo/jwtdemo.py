
#https://www.geeksforgeeks.org/using-jwt-for-user-authentication-in-flask/
#https://www.geeksforgeeks.org/connect-flask-to-a-database-with-flask-sqlalchemy/?ref=rp

import jwt
from datetime import  *

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

value = encodeJwtToken()
print(value)
decoded_value = decodeJWToken(value)
print(decoded_value)

'''
value = jwt.decode(encoded, "secret", algorithms=["HS256"])
print(value)
payload = {"some": "payload", "aud": ["urn:foo", "urn:bar"]}

token = jwt.encode(payload, "secret")
decoded = jwt.decode(token, "secret", audience="urn:foo", algorithms=["HS256"])
'''

#jwt.decode(encoded, options={"verify_signature": False})

