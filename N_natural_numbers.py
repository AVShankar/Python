#Write a program to print the sum of the first K natural numbers.

n=int(input())
result=0
if(n <= 100000):
	result=(n*(n+1))/2
	print(result)
