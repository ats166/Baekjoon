import math
def prime(num):
	for i in range(2,int(math.sqrt(num))+1):
		if num % i == 0:
			return False
	return True
    
def check(num):
	visit = {}
	while 1:
		n = str(num)
		num = 0
		for i in range(len(n)):
			num += int(n[i]) ** 2
		if num == 1:
			return True

		if num in visit:
			return False
		else:
			visit[num] = 1
		
n = int(input())
for i in range(7,n+1):
	if prime(i):  # 소수인지 확인
		if check(i): # 상근수인지 확인
			print(i)