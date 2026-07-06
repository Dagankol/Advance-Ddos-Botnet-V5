import base64, json
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

data = {"iv": "UFCsfHHJFi427o09jXVdiA==", "ct": "euIUeN6EYzViQGGJ7AtUoo>

iv = base64.b64decode(data['iv'])
ct = base64.b64decode(data['ct'])
key = base64.b64decode(data['key'])

cipher = AES.new(key, AES.MODE_CBC, iv)
plain = unpad(cipher.decrypt(ct), AES.block_size)
exec(plain)
