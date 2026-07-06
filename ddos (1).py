import base64, json
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

data = {"iv": "0MfrRViGr0TYpftSym/ttQ==", "ct": "3TCFhy/G9JpQkiVEYmpIhO>

iv = base64.b64decode(data['iv'])
ct = base64.b64decode(data['ct'])
key = base64.b64decode(data['key'])

cipher = AES.new(key, AES.MODE_CBC, iv)
plain = unpad(cipher.decrypt(ct), AES.block_size)
exec(plain)
