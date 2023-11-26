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

"""
DEBUG OUTPUT:
    12pKXaXAFi+vwsgYUPmqsqxYuWN59MkSi7BRSWodJjwDO3zo6Hx8XdVanLmxP4TW
    omQsgla6+SkOA9sj4A1xI1wEcU6CftcACWRcO1f2Gv9/9UetdxV5JP8StOkR8XQd48Nv/RUewJp8ziMDWRsCig==
    O/pGZxJl5B7jAL2Eh1Vn+R0YLyLmWBNyV+GEMbjajdUOk84GoB7jy7JHRvOHObbxMN2kln48ZVLksisS9VH1B8Cef+pV4Ot+mnazHN5DUKU=
    +xPWg49x4M/dEa8ZhkvBOhF3PSmg6qeb/0ip1UKPuXeoGLmfydcU9ygF0VPK/tzeoJr8YCIr2kXjrHNFbNjXwA==
    Bp+0I+tqPqTM7O59L8Pr7eu9g7pn596fhsxGDu8Ujwr247SLc5EIRlQ3uToyo04faAtIS7VVoRShXQ9VjB+qaA==
    Bp+0I+tqPqTM7O59L8Pr7eu9g7pn596fhsxGDu8Ujwr247SLc5EIRlQ3uToyo04faAtIS7VVoRShXQ9VjB+qaA==
    JOeWQ50aYiEu8MnEVaWqwSHjX9/Tlwd+yz/LcNJT+NyBEw20H/jj6K/sR4fCJSd2LntdiYogLqaP9itjpVdvEw==
"""
