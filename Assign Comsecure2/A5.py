#Ref : https://gist.github.com/lkdocs/6519378
#Ref : https://stackoverflow.com/questions/28426102/python-crypto-rsa-public-private-key-with-large-file
#Ref : https://www.pythonsheets.com/notes/python-crypto.html
#Ref : https://www.pythonsheets.com/notes/python-crypto.html

from Crypto.PublicKey import RSA 
import time
from cryptography.fernet import Fernet
import base64
from Crypto.Cipher import PKCS1_OAEP

prevTime = 0
BLOCKSIZE = 128
cipher_text = "".encode()
def timeStop():
    global prevTime
    currentTime = time.time()
    diffTime = currentTime - prevTime
    prevTime = currentTime
    return diffTime

def generate_RSA(bits):

    new_key = RSA.generate(bits, e=65537) 
    public_key = new_key.publickey()
    private_key = new_key 
    return private_key, public_key
    #return public_key

def encrypt(file_name,cipher):
    global cipher_text
    with open(file_name, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            cipher_text = cipher.encrypt("hello".encode())
            #cipher_text = cipher.encrypt(str(buf).encode())
            buf = afile.read(BLOCKSIZE)
    
private_key2048,public_key2048 = generate_RSA(2048)
private_key3072,public_key3072 = generate_RSA(3072)
private_key4096,public_key4096 = generate_RSA(4096)

cipher2048Bit = PKCS1_OAEP.new(public_key2048)
cipher3072Bit = PKCS1_OAEP.new(public_key3072)
cipher4096Bit = PKCS1_OAEP.new(public_key4096)

print("Gen key complete")

#cipher_text = cipher2048Bit.encrypt(file100MB)

#print(cipher_text)

temp = timeStop()

encrypt('out100MB.txt',cipher2048Bit)
print("Time to encrypt 100 MB with key 2048 Bit is : " + str(timeStop()))

encrypt('out200MB.txt',cipher2048Bit)
print("Time to encrypt 200 MB with key 2048 Bit is : " + str(timeStop()))

encrypt('out300MB.txt',cipher2048Bit)
print("Time to encrypt 300 MB with key 2048 Bit is : " + str(timeStop()))

encrypt('out400MB.txt',cipher2048Bit)
print("Time to encrypt 400 MB with key 2048 Bit is : " + str(timeStop()))

#///////////////////////////////////////////////////////////////////

encrypt('out100MB.txt',cipher3072Bit)
print("Time to encrypt 100 MB with key 3072 Bit is : " + str(timeStop()))

encrypt('out200MB.txt',cipher3072Bit)
print("Time to encrypt 200 MB with key 3072 Bit is : " + str(timeStop()))

encrypt('out300MB.txt',cipher3072Bit)
print("Time to encrypt 300 MB with key 3072 Bit is : " + str(timeStop()))

encrypt('out400MB.txt',cipher3072Bit)
print("Time to encrypt 400 MB with key 3072 Bit is : " + str(timeStop()))

#///////////////////////////////////////////////////////////////////

encrypt('out100MB.txt',cipher4096Bit)
print("Time to encrypt 100 MB with key 4096 Bit is : " + str(timeStop()))

encrypt('out200MB.txt',cipher4096Bit)
print("Time to encrypt 200 MB with key 4096 Bit is : " + str(timeStop()))

encrypt('out300MB.txt',cipher4096Bit)
print("Time to encrypt 300 MB with key 4096 Bit is : " + str(timeStop()))

encrypt('out400MB.txt',cipher4096Bit)
print("Time to encrypt 400 MB with key 4096 Bit is : " + str(timeStop()))

#///////////////////////////////////////////////////////////////////
'''