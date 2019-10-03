#Given a number N and array of N integers, print the difference between the smallest and largest number

N = int(input())
n = list(map(int,input().split()))

for i in range (0, N):
    for j in range (0, N):
        if(n[i] < n[j]):
            temp = n[i]
            n[i] = n[j]
            n[j] = temp

print((n[0] - n[N-1])*-1)
