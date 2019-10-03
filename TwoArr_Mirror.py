#Check whether the given array are mirror of each other

N = int(input())
arr1 = list(map(int, input().split()[:N]))
arr2 = list(map(int, input().split()[:N]))
count = 0

if(N <= 1000000):
    for i in arr1:
        for j in reversed (arr2):
            if(i == j):
                count += 1
            else:
                continue

if(count == N):
    print('yes')

else:
    print('no')
