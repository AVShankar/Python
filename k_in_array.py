#Given 2 numbers N and K followed by n numbers check if K exists

count=0
N, K = map(int, input().split())
n=list(map(int, input().split()[:N]))
for i in range (0, N):
    if(n[i]==K):
        print("yes")
        count+=1
        break
if(count==0):
        print("no")
