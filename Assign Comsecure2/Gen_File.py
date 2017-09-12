import random

SIZE_OF_RANDOM = 3000

file = open('out3G.txt', 'w')
for y in range(int(SIZE_OF_RANDOM)):
	print(y)
	for x in range(53500):
		file.write(str(random.random())+'\n')