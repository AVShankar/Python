#Sort and print addition ele one and two

N = int(input())
n = list(map(int, input().split()[:N]))
for i in range (0, N):
        for j in range (1, N):
            if(n[j] < n[j-1]):
                if(i != N-1):
                    temp = n[j]
                    n[j] = n[j-1]
                    n[j-1] = temp
print(n[0] + n[1])
