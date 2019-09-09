#Given an array of numbers switch(swap) the adjacent characters

N=int(input())
n=list(map(int, input().split()[:N]))
for i in range (0, N, 2):
  if(i==N-1):
    break
  else:
  	temp = n[i]
  	n[i] = n[i+1]
  	n[i+1] = temp

for i in range (0, N):
  print(n[i], end=" ")
