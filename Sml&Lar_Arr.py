#Given a number N followed by N numbers. Find the smallest number and largest number and print both the indices(1based indexing)

N=int(input())
K=list(map(int, input().split()[:N]))
length = len(K)

if(N <= 100000):
    for i in range (0, N):
        for j in range (1, N):
            if(K[j] < K[j-1]):
                temp = K[j]
                K[j] = K[j-1]
                K[j-1] = temp

for i in range (0, N):
    if(i==0):
        print(K[i], end=" ")
    if(i==N-1):
        print(K[i])
