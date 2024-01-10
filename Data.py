#Data.py

import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import random

class MCrypt:
    def __init__(self):
        self.iv = bytes([49, 50, 51, 52, 53, 54, 55, 56, 57, 48, 49, 50, 51, 52, 53, 54])
        self.SecretKey = b"QWERTYUIOPCVBN54QWERTYUIOPCVBN54"
        self.ivspec = self.iv
        self.keyspec = self.SecretKey
        self.cipher = AES.new(self.keyspec, AES.MODE_CBC, self.ivspec)

    def encrypt(self, str):
        cipher = AES.new(self.keyspec, AES.MODE_CBC, self.ivspec)
        encrypted = cipher.encrypt(pad(str.encode(), AES.block_size))
        return base64.b64encode(encrypted).decode()

    def decrypt(self, str):
        if str is None or len(str) == 0:
            raise Exception("Empty string")
        decrypted = self.cipher.decrypt(base64.b64decode(str))
        return unpad(decrypted, AES.block_size).decode()


def data():
  m = MCrypt()
  t = "\"{ \\\"coins\\\" : \\\"5\\\",\\\"spin\\\" : \\\"true\\\",\\\"tranId\\\" : \\\""+str(random.randint(0,999999)+111111)+"\\\"}\""
 # print(t)
  return m.encrypt(t)
