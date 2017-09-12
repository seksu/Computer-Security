import hashlib
import random
import matplotlib.pyplot as plt
import numpy as np
import math
import time

BLOCKSIZE = 65536
prevTime = 0

def timeStop():
	global prevTime
	currentTime = time.time()
	diffTime = currentTime - prevTime
	prevTime = currentTime
	return diffTime

temp = timeStop()
hasher = hashlib.sha1()
with open('out1G.txt', 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)
print("Hash file 1 GB(sha1)\t\t: " + str(hasher.hexdigest()))
print("TimeStop file 1 GB(sha1)\t: " + str(timeStop()) + " sec\n")

#/////////////////////////////////////////////////

temp = timeStop()
hasher = hashlib.sha1()
with open('out2G.txt', 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)
print("Hash file 2 GB(sha1)\t\t: " + str(hasher.hexdigest()))
print("Time Stop file 2 GB(sha1)\t: " + str(timeStop()) + " sec\n")

#/////////////////////////////////////////////////

temp = timeStop()
hasher = hashlib.sha1()
with open('out3G.txt', 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)
print("Hash file 3 GB(sha1)\t\t: " + str(hasher.hexdigest()))
print("Time Stop file 3 GB(sha1)\t: " + str(timeStop()) + " sec\n")

#/////////////////////////////////////////////////

temp = timeStop()
hasher = hashlib.sha1()
with open('out4G.txt', 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)
print("Hash file 4 GB(sha1)\t\t: " + str(hasher.hexdigest()))
print("Time Stop file 4 GB(sha1)\t: " + str(timeStop()) + " sec\n")

#/////////////////////////////////////////////////

temp = timeStop()
hasher = hashlib.md5()
with open('out1G.txt', 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)
print("Hash file 1 GB(md5)\t\t\t: " + str(hasher.hexdigest()))
print("Time Stop file 1 GB(md5)\t: " + str(timeStop()) + " sec\n")

#/////////////////////////////////////////////////

temp = timeStop()
hasher = hashlib.md5()
with open('out2G.txt', 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)
print("Hash file 2 GB(md5)\t\t\t: " + str(hasher.hexdigest()))
print("Time Stop file 2 GB(md5)\t: " + str(timeStop()) + " sec\n")

#/////////////////////////////////////////////////

temp = timeStop()
hasher = hashlib.md5()
with open('out3G.txt', 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)
print("Hash file 3 GB(md5)\t\t\t: " + str(hasher.hexdigest()))
print("Time Stop file 3 GB(md5)\t: " + str(timeStop()) + " sec\n")

#/////////////////////////////////////////////////

temp = timeStop()
hasher = hashlib.md5()
with open('out4G.txt', 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)
print("Hash file 4 GB(md5)\t\t\t: " + str(hasher.hexdigest()))
print("Time Stop file 4 GB(md5)\t: " + str(timeStop()) + " sec\n")

#/////////////////////////////////////////////////