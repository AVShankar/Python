#Given a number N, find its factorial.

fact = 1
N = int(input())
if( N <= 20):
  while(N!=0):
  	fact = fact * N
  	N=N-1

print(fact)
