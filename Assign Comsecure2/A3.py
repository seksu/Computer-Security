#Ref : http://docs.python-guide.org/en/latest/scenarios/crypto/ 
#Ref : http://pynacl.readthedocs.io/en/latest/secret/

from Crypto.Cipher import AES
from cryptography.fernet import Fernet
import base64

key = 'AAAAB3NzaC1yc2EAAAABJQAAACEAmfDY'
keyBase64 = base64.b64encode(b'AAAAB3NzaC1yc2EAAAABJQAAACEAmfDY')

# Encryption
encryption_suite = AES.new(key, AES.MODE_CBC, 'This s IV Mute16')
cipher_text = encryption_suite.encrypt("abcdefghijklmnop")

# Decryption
decryption_suite = AES.new(key, AES.MODE_CBC, 'This s IV Mute16')
plain_text = decryption_suite.decrypt(cipher_text)

print("key is(AES) : " + str(key))
print("cipher_text is(AES Algo) : " + str(cipher_text))
print("plain_text is(AES Algo)  : " + str(plain_text))
print()

#//////////////////////////////////////

#key = Fernet.generate_key()

print("key is(base64) : " + str(keyBase64))

cipher_suite = Fernet(keyBase64)
cipher_text = cipher_suite.encrypt(b"A really secret message. Not for prying eyes.")
plain_text = cipher_suite.decrypt(cipher_text)

print("cipher_text is(Fernet Algo) : " + str(cipher_text))
print("plain_text is(Fernet Algo)  : " + str(plain_text))