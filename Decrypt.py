import math
import secrets
import string
import base64
import pickle
from Signature import Signature
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from bz2 import BZ2File

class Decrypt:
	def __init__(self):
		self.privateKeyPath = None
		self.cipherTextPath = None

	def setPrivateKeyPath(self, filePath):
		self.privateKeyPath = filePath

	def setCipherTextPath(self, filePath):
		self.cipherTextPath = filePath

	def loadKey(self, path):
		file = BZ2File(path, 'r')
		key = pickle.load(file)
		file.close()
		return key

	def AES_KeyDecryption(self, privateKey, encrypedSecret):
		privateKey = PKCS1_OAEP.new(privateKey)
		return privateKey.decrypt(encrypedSecret)


	def decrypter(self):
		try:
			privateKey = self.loadKey(self.privateKeyPath)
			cipherText = self.loadKey(self.cipherTextPath)
		except:
			exit()
		encrypedSecret = cipherText[1]
		encryptedImage = cipherText[2]
		privateKey = RSA.importKey(privateKey)

		decryptedSecret = self.AES_KeyDecryption(privateKey, encrypedSecret)
		AES_Key = AES.new(decryptedSecret, AES.MODE_CBC, iv = cipherText[0])
		with open("RESULT.jpg", "wb") as image:
			image.write(base64.b64decode(AES_Key.decrypt(encryptedImage)))
		self.verify()	

	def verify(self):
		digest = self.loadKey(self.cipherTextPath)[3]
		sign = Signature('RESULT.jpg')
		print(sign.verifySignature(digest))

