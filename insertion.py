import random
import time
import matplotlib.pyplot as plt
import numpy as np

def insertion(x):

	for i in range (1, len(x)):
		key = x[i]

		j = i - 1
		while j >= 0 and key < x[j]:
			x[j+1] = x[j]
			j -= 1
		x[j + 1] = key

graphTime = []
graphLimit = []
def recordGraph():
	x = []
	limit = int(input("Limit of the array: "))
	graphLimit.append(limit)
	k = 0
	while k != limit:
		x.append(random.randrange(0,limit))
		k = k + 1
	sortStart = time.time()
	print("sorted:")
	insertion(x)
	print(x)
	sortEnd = time.time()
	sortTime = sortEnd - sortStart
	graphTime.append(sortTime)
	print("Time elapsed ", round(sortTime)," secs")
	Q = input("would you like to run another test?(y/n): ")
	if Q == 'y':
		recordGraph()
	else:
		print("results of the tests in order: \n")

recordGraph()
print("limits: ", graphLimit)
print("results in time: ",graphTime)
print("please wait for the graph.....")
plt.plot(graphLimit,graphTime, color='red', linewidth=1)
plt.show()
