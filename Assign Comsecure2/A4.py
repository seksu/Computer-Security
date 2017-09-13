#Ref : https://gist.github.com/lkdocs/6519378
from Crypto.PublicKey import RSA 
import time
prevTime = 0

def timeStop():
    global prevTime
    currentTime = time.time()
    diffTime = currentTime - prevTime
    prevTime = currentTime
    return diffTime

def generate_RSA(bits):

    new_key = RSA.generate(bits, e=65537) 
    public_key = new_key.publickey().exportKey("PEM") 
    #private_key = new_key.exportKey("PEM") 
    #return private_key, public_key
    return public_key

temp = timeStop()
#print(str(generate_RSA(2048)) + "\n")
temp = generate_RSA(2048)
print("Time Stop is(2048 Bit) : " + str(timeStop()) + "\n")

temp = timeStop()
#print(str(generate_RSA(3072)) + "\n")
temp = generate_RSA(3072)
print("Time Stop is(3072 Bit) : " + str(timeStop()) + "\n")

temp = timeStop()
#print(str(generate_RSA(4096)) + "\n")
temp = generate_RSA(4096)
print("Time Stop is(4096 Bit) : " + str(timeStop()) + "\n")
