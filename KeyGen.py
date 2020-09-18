import math
import secrets
import string
import base64
import pickle
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from bz2 import BZ2File
from random import randint

class KeyGen:
    def generateRsaKey(self):
        rsa = RSA.generate(2048)
        self.privateKey = rsa
        self.publicKey = rsa.publickey()
        self.storeKeys()

    def saveKey(self, fileName, key):
        file = BZ2File(fileName, 'w')
        pickle.dump(key.exportKey(), file)
        file.close()

    def storeKeys(self):
        randomInt = randint(0, 100)
        fileName = 'Private Key'
        self.saveKey(fileName, self.privateKey)
        fileName = 'Public Key' 
        self.saveKey(fileName, self.publicKey)

