#Given 2 numbers N and K followed by n numbers print the number of repetitions of K

count=0
N, K = map(int, input().split())
n=list(map(int, input().split()[:N]))
for i in range (0, N):
    if(n[i]==K):
        count+=1

print(count)
