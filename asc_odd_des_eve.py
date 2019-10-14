#Sorting asc odd and desc even

N = int(input())
n = list(map(int, input().split()[:N]))
for i in range (0, N):
    if(i%2 == 0):
        for j in range (2, N, 2):
            if(n[j] < n[j-2]):
                if(i != N-1):
                    temp = n[j]
                    n[j] = n[j-2]
                    n[j-2] = temp
    else: 
        for j in range (3, N, 2):
            if(n[j] > n[j-2]):
                if(i != N-1):
                    temp = n[j]
                    n[j] = n[j-2]
                    n[j-2] = temp
for i in range (0, N):
    print(n[i], end=" ")
