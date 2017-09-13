#Ref : http://pynacl.readthedocs.io/en/latest/signing/
import nacl.encoding
import nacl.signing
import time

prevTime = 0
BLOCKSIZE = 125000

def timeStop():
    global prevTime
    currentTime = time.time()
    diffTime = currentTime - prevTime
    prevTime = currentTime
    return diffTime

def signning(key,file_name):
	with open(file_name, 'rb') as afile:
		buf = afile.read(BLOCKSIZE)
		while len(buf) > 0:
			key.sign(buf)
			buf += afile.read(BLOCKSIZE)

# Generate a new random signing key
signing_key = nacl.signing.SigningKey.generate()

# Sign a message with the signing key
signed = signing_key.sign(b"Attack at Dawn")

# Obtain the verify key for a given signing key
verify_key = signing_key.verify_key

# Serialize the verify key to send it to a third party
verify_key_hex = verify_key.encode(encoder=nacl.encoding.HexEncoder)

#print(verify_key.verify(signed))
temp = timeStop()
#signed = signing_key.sign(open('out1G.txt', 'rb').read())
signed = signning(signing_key,'out1G.txt')
print("timeStop to sign file 1 GB is : " + str(timeStop()))

temp = timeStop()
#signed = signing_key.sign(open('out2G.txt', 'rb').read())
signed = signning(signing_key,'out2G.txt')
print("timeStop to sign file 2 GB is : " + str(timeStop()))

temp = timeStop()
signed = signing_key.sign(open('out3G.txt', 'rb').read())
print("timeStop to sign file 3 GB is : " + str(timeStop()))

temp = timeStop()
signed = signing_key.sign(open('out4G.txt', 'rb').read())
print("timeStop to sign file 4 GB is : " + str(timeStop()))
