#Ref : https://www.dlitz.net/software/pycrypto/doc/#crypto-publickey-public-key-algorithms
from Crypto.Hash import MD5
from Crypto.PublicKey import RSA
from Crypto import Random

BLOCKSIZE = 128

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
    return private_key, public_key ,new_key 

def signning(file_name,key):
	global cipher_text
	with open(file_name, 'rb') as afile:
		buf = afile.read(BLOCKSIZE)
		while len(buf) > 0:
			rng = Random.new().read
			hash = MD5.new(str(buf).encode()).digest()
			#cipher_text = cipher.encrypt(str(buf).encode())
			signature = key.sign(hash,rng)
			buf = afile.read(BLOCKSIZE)

private_key2048,public_key2048,key2048 = generate_RSA(2048)
private_key3072,public_key3072,key3072 = generate_RSA(3072)
private_key4096,public_key4096,key4096 = generate_RSA(4096)


temp = timeStop()
signning('out1G.txt',key2048)
print("timeStop to sign file 1 GB with key 2048 Bit is : " + str(timeStop()))

signning('out2G.txt',key2048)
print("timeStop to sign file 2 GB with key 2048 Bit is : " + str(timeStop()))

signning('out3G.txt',key2048)
print("timeStop to sign file 3 GB with key 2048 Bit is : " + str(timeStop()))

signning('out4G.txt',key2048)
print("timeStop to sign file 4 GB with key 2048 Bit is : " + str(timeStop()))

signning('out1G.txt',key3072)
print("timeStop to sign file 1 GB with key 3072 Bit is : " + str(timeStop()))

signning('out2G.txt',key3072)
print("timeStop to sign file 2 GB with key 3072 Bit is : " + str(timeStop()))

signning('out3G.txt',key3072)
print("timeStop to sign file 3 GB with key 3072 Bit is : " + str(timeStop()))

signning('out4G.txt',key3072)
print("timeStop to sign file 4 GB with key 3072 Bit is : " + str(timeStop()))

signning('out1G.txt',key4096)
print("timeStop to sign file 1 GB with key 4096 Bit is : " + str(timeStop()))

signning('out2G.txt',key4096)
print("timeStop to sign file 2 GB with key 4096 Bit is : " + str(timeStop()))

signning('out3G.txt',key4096)
print("timeStop to sign file 3 GB with key 4096 Bit is : " + str(timeStop()))

signning('out4G.txt',key4096)
print("timeStop to sign file 4 GB with key 4096 Bit is : " + str(timeStop()))

'''
plaintext = 'hello'.encode()
rng = Random.new().read
RSAkey = RSA.generate(1024, rng)   # This will take a while...
hash = MD5.new(plaintext).digest()
signature = RSAkey.sign(hash, rng)
RSAkey.verify(hash, signature)
'''

