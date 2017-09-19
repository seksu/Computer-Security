import random

SIZE_OF_RANDOM = 400

file = open('out400MB.txt', 'w')
for y in range(int(SIZE_OF_RANDOM)):
	print(y)
	for x in range(53500):
		file.write(str(random.random())+'\n')