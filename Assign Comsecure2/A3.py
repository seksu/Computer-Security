#Ref : http://docs.python-guide.org/en/latest/scenarios/crypto/ 
#Ref : http://pynacl.readthedocs.io/en/latest/secret/

from Crypto.Cipher import AES
from cryptography.fernet import Fernet
import base64
import time

prevTime = 0
BLOCKSIZE = 16

key = 'AAAAB3NzaC1yc2EAAAABJQAAACEAmfDY'
keyBase64 = base64.b64encode(b'AAAAB3NzaC1yc2EAAAABJQAAACEAmfDY')
encryption_suite = AES.new(key, AES.MODE_CBC, 'This s IV Mute16')

cipher_suite = Fernet(keyBase64)

def timeStop():
    global prevTime
    currentTime = time.time()
    diffTime = currentTime - prevTime
    prevTime = currentTime
    return diffTime

def AESEncrypt(file_name):
	with open(file_name, 'rb') as afile:
		buf = afile.read(BLOCKSIZE)
		while len(buf) > 0:	
			cipher_text = encryption_suite.encrypt(buf)
			buf = afile.read(BLOCKSIZE)    

def FernetEncrypt(file_name):
	with open(file_name, 'rb') as afile:
		buf = afile.read(BLOCKSIZE)
		while len(buf) > 0:
			print(buf)
			cipher_text = cipher_suite.encrypt(buf)
			buf = afile.read(BLOCKSIZE) 


temp = timeStop()
AESEncrypt('out1G.txt')
print("Time to Encrypt file 1 GB with AES is : " + timeStop())
AESEncrypt('out2G.txt')
print("Time to Encrypt file 2 GB with AES is : " + timeStop())
AESEncrypt('out3G.txt')
print("Time to Encrypt file 3 GB with AES is : " + timeStop())
AESEncrypt('out4G.txt')
print("Time to Encrypt file 4 GB with AES is : " + timeStop())

FernetEncrypt('out1G.txt')
print("Time to Encrypt file 1 GB with Fernet is : " + timeStop())
FernetEncrypt('out2G.txt')
print("Time to Encrypt file 2 GB with Fernet is : " + timeStop())
FernetEncrypt('out3G.txt')
print("Time to Encrypt file 3 GB with Fernet is : " + timeStop())
FernetEncrypt('out4G.txt')
print("Time to Encrypt file 4 GB with Fernet is : " + timeStop())

'''
decryption_suite = AES.new(key, AES.MODE_CBC, 'This s IV Mute16')
plain_text = decryption_suite.decrypt(cipher_text)

print("\nkey is(AES) 					: " + str(key))
#print("\ncipher_text is(AES Algo) 		: " + str(cipher_text))
print("\nplain_text is(AES Algo)  		: " + str(plain_text))
print()

#//////////////////////////////////////

#key = Fernet.generate_key()

print("key is(Fernet) 					: " + str(keyBase64))

cipher_suite = Fernet(keyBase64)
cipher_text = cipher_suite.encrypt(b"This is plain text")
plain_text = cipher_suite.decrypt(cipher_text)

print("\ncipher_text is(Fernet Algo) 	: " + str(cipher_text))
print("\nplain_text is(Fernet Algo)  	: " + str(plain_text))
'''