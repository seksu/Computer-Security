import hashlib
import random
import matplotlib.pyplot as plt
import numpy as np
import math

SIZE_OF_RANDOM = 10000000

averageRand  = 0
averageHash  = 0
averageHash2 = 0

sumData = 0

varRand = []
varHash = []
varHash2= []

frand = open('outrand.txt', 'w')
fhash = open('outhash.txt', 'w')
fhash2= open('outhash2.txt','w')

random.seed(1)

def sd(data,xbar):
	#print("test : " + str(data[1]-xbar))
	sumData = 0
	for x in range(SIZE_OF_RANDOM):
		global sumData
		sumData = sumData+((data[x]-xbar)**(data[x]-xbar))
	return math.sqrt((sumData/len(data)).real)

for x in range(SIZE_OF_RANDOM):
	varRand.append(random.random())
	averageRand = (averageRand+varRand[x])/2
	frand.write(str(varRand[x])+'\n')
	print(varRand[x])

plt.subplot(311)
#plt.plot(varRand[:])
xx = np.arange(SIZE_OF_RANDOM)
plt.hist(varRand[:])

#plt.scatter(xx,varRand[0:SIZE_OF_RANDOM],s=0.25)

#///////////////////// Hash sha512 //////////////////////

hashGen = hashlib.sha512()

for x in range(SIZE_OF_RANDOM):
	hashGen.update(str(x).encode('utf-8'))
	hash = (int(hashGen.hexdigest(),16)/10e+154)
	varHash.append(hash)
	averageHash = (averageHash+varHash[x])/2
	fhash.write(str(varHash[x]) + '\n')
	print(varHash[x])


plt.subplot(312)
#plt.plot(varHash[:])
plt.hist(varHash[:])
#plt.scatter(xx,varHash[0:SIZE_OF_RANDOM],s=0.25)
#plt.show()

#//////////////////// Hash md5 /////////////

hashGen2 = hashlib.md5()

for x in range(SIZE_OF_RANDOM):
	hashGen2.update(str(x).encode('utf-8'))
	hash = (int(hashGen2.hexdigest(),16)/10e+38)
	varHash2.append(hash)
	averageHash2 = (averageHash2+varHash2[x])/2
	fhash2.write(str(varHash2[x]) + '\n')
	print(varHash2[x])

plt.subplot(313)
#plt.plot(varHash2[:])
plt.hist(varHash2[:])
#plt.scatter(xx,varHash2[0:SIZE_OF_RANDOM],s=0.25)


#////////////////// sumary /////////////////

print("")
print("Avg(Rand)        : " + str(averageRand))
print("SD(Rand)         : " + str(sd(varRand,averageRand)))

print("AVG(Hash Sha512) : " + str(averageHash))
print("SD(Hash Sha512)  : " + str(sd(varHash,averageHash)))

print("AVG(Hash md5)    : " + str(averageHash2))
print("SD(Hash md5)     : " + str(sd(varHash2,averageHash2)))

plt.show()