

N = int(input())
n = list(map(int, input().split()[:N]))
K = int(input())
k = list(map(int, input().split()[:K]))
count = 0
if(N <= 1000 and K <= 1000):
    if(N >=1 and K >=1):
        for i in range (0, K): 
            for j in range (0, N):
                if(k[i] == n[j]): 
                    count+=1
            if(count == 0):
                print("Not Present", end=" ")
            else:
                print(count, end=" ")
            count = 0
