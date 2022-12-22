from jose import jwt
from jose import jwe
from jwcrypto import jwk, jwe
from jwcrypto.common import json_encode


with open("privatekey.pem", "rb") as pemfile:
    privKey = jwk.JWK.from_pem(pemfile.read())

with open("publickey.pem", "rb") as pemfile:
    pubKey = jwk.JWK.from_pem(pemfile.read())

claims= {'key':'value','key2':'value2'}

token = jwt.encode(claims, privKey, algorithm='RS256')


# algorithm to use
eprot = {'alg': "RSA-OAEP-256", 'enc': "A256CBC-HS512"}
stringPayload = token
E = jwe.JWE(stringPayload, json_encode(eprot))
E.add_recipient(pubKey)
encrypted_token = E.serialize(compact=True)

print(encrypted_token)