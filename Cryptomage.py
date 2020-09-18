from KeyGen import KeyGen
from Encrypt import Encrypt
from Decrypt import Decrypt

assymetricKey = KeyGen()
assymetricKey.generateRsaKey()

encrypt = Encrypt()
encrypt.setImagePath("spiderman.jpg")
encrypt.setPublicKeyPath("Public Key")
encrypt.encrypter()

decrypt = Decrypt()
decrypt.setPrivateKeyPath("Private Key")
decrypt.setCipherTextPath("Cipher Text")
decrypt.decrypter()

