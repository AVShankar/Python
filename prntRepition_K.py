#Given 2 numbers N and K followed by N elements,print the number of repetition of K otherwise print '-1' if the element not found

N, K = map(int, input().split())
n = list(map(int, input().split()[:N]))
count = 0

for i in range (0, N):
  if(n[i] == K):
    count += 1
    
if(count==1):
  print(0)
else:
  print(-1)
