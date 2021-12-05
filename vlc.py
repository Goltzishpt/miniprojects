import time
start_time = time.time()

n = int(input())
counter = 1
for i in range(1, n + 1):
	for j in range(1, counter + 1):
		print(j, end = '')
	for k in range(1, counter + 1):
		if j - k == 0:
			break
		print(j - k, end = '')
	counter += 1
	print()	


print("--- %s seconds ---" % (time.time() - start_time))