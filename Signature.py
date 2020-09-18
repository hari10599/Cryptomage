import hashlib
import base64

class Signature:
	def __init__(self, filePath):
		self.filePath = filePath

	def imageToBase64(self):
		image = open(self.filePath, 'rb')
		try:
			encodedImage = base64.b64encode(image.read())
		except:
			encodedImage = ""
		return encodedImage

	def generateSignature(self):
		signature = hashlib.sha512(self.imageToBase64())
		return signature.hexdigest()

	def verifySignature(self, clientSignature):
		signature = self.generateSignature()
		return clientSignature == signature

