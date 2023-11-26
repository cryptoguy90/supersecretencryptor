# -*- coding: utf-8 -*-

import os, sys
from AES import AESCipher

KEY = os.environ.get("AES_KEY", "supersecretkey")

mode, string = sys.argv[1:3]

aes = AESCipher(KEY)

if mode == "encrypt":
    print(aes.encrypt(string))
else:
    print(aes.decrypt(string))
