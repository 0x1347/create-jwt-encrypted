from jose import jwt
from jose import jwe
from jwcrypto import jwk, jwe
from jwcrypto.common import json_encode



# open both the private and the public keys
with open("privatekey.pem", "rb") as pemfile:
    privKey = jwk.JWK.from_pem(pemfile.read())
with open("publickey.pem", "rb") as pemfile:
    pubKey = jwk.JWK.from_pem(pemfile.read())


def generateJWT(claims):  
    # create jwt token with RS256 algorithm 
    token = jwt.encode(claims, privKey, algorithm='RS256')
    return token

def generateJWE(jsonWebToken):
    # algorithm to use
    eprot = {'alg': "RSA-OAEP-256", 'enc': "A256CBC-HS512"}
    enc = jwe.JWE(jsonWebToken, json_encode(eprot))
    enc.add_recipient(pubKey)
    encrypted_token = enc.serialize(compact=True)
    return encrypted_token


if __name__ == "__main__":
    claims= {
        'key':'value',
        'key2':'value2'
        }
    jsonWebToken = generateJWT(claims)
    encryptedjsonWebToken = generateJWE(jsonWebToken)
    print(encryptedjsonWebToken)