import math
import secrets
import string
import base64
import pickle
from Signature import Signature
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from bz2 import BZ2File
from random import randint


class Encrypt:
	def __init__(self):
		self.publicKeyPath = None
		self.AES_Key = None
		self.secret = None
		self.imagePath = None

	def setPublicKeyPath(self, filePath):
		self.publicKeyPath = filePath

	def setImagePath(self, filePath):
		self.imagePath = filePath

	def imageToBase64(self):
		image = open(self.imagePath, 'rb')
		try:
			encodedImage = base64.b64encode(image.read())
		except:
			encodedImage = ""
		return encodedImage

	def loadKey(self):
		file = BZ2File(self.publicKeyPath, 'r')
		key = pickle.load(file)
		file.close()
		return key

	def save(self, encryption):
		file = BZ2File('Cipher Text', 'w')
		pickle.dump(encryption, file)
		file.close()		

	def generateAesKey(self):
		secret = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(16))
		self.secret = secret
		secret = bytes(secret, 'utf-8')
		self.AES_Key = AES.new(secret, AES.MODE_CBC)

	def AES_KeyEncryption(self, publicKey):
		publicKey = PKCS1_OAEP.new(publicKey)
		return publicKey.encrypt(self.secret.encode())


	def encrypter(self):
		self.generateAesKey()
		encodedImage = self.imageToBase64() #bytes
		image = encodedImage.decode() #string
		paddingLength = math.ceil(len(image)/16)*16 - len(image)
		image = image + " " * paddingLength
		encryptedImage = self.AES_Key.encrypt(image.encode())
		

		publicKey = RSA.importKey(self.loadKey())
		encryptedAES = self.AES_KeyEncryption(publicKey)
		sign = Signature(self.imagePath)

		encryption = []
		encryption.append(self.AES_Key.iv)
		encryption.append(encryptedAES)
		encryption.append(encryptedImage)
		encryption.append(sign.generateSignature())
		self.save(encryption)



