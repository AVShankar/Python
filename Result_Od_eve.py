#Given 2 numbers N and M add it and check whether the result is odd or even.

N, M = map(int, input().split())
if((N+M) %2==0):
	print("even")        
else:
	print("odd")
