import random
import time
import matplotlib.pyplot as plt
import numpy as np

def merge(x):
	if len(x) >1:
		mid = len(x)//2
		L = x[:mid]
		R = x[mid:]

		merge(L)
		merge(R)

		i = j = k = 0

		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				x[k] = L[i]
				i+=1
			else:
				x[k] = R[j]
				j+=1
			k+=1

		while i < len(L):
			x[k] = L[i]
			i+=1
			k+=1

		while j < len(R):
			x[k] = R[j]
			j+=1
			k+=1

graphTime = []
graphLimit = []
def recordGraph():
	x = []
	k = 0
	limit = int(input("Limit of the array: "))
	graphLimit.append(limit)
	while k != limit:
		x.append(random.randrange(0,limit))
		k = k + 1

	merge(x)
	sortStart = time.time()
	print("na sort na: ")
	print(x)
	sortEnd = time.time()
	sortTime = sortEnd - sortStart
	graphTime.append(sortTime)
	print("Time elapsed for sorted: ",round(sortTime)," seconds")
	Q = input("would you like to run another test?(y/n): ")
	if Q == 'y':
		recordGraph()
	else:
		print("results of the tests in order: \n")

recordGraph()
print("limits: ", graphLimit)
print("time results: ", graphTime)
print("please wait for the graph.....")
plt.plot(graphLimit,graphTime, color = 'green', linewidth=1)
plt.show()