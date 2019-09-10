#Union of two array and sort the result

n = int(input())
arr1 = list(map(int, input().split()[:n]))
k = int(input())
arr2 = list(map(int, input().split()[:k]))
def union(lst1, lst2):
    return list(set(lst1) | set(lst2))

result = union(arr1, arr2)
length = len(result)
for i in range(0, length):
    for j in range(1, length):
        if(result[j] < result[j-1]):
            temp = result[j]
            result[j] = result[j-1]
            result[j-1] = temp

for i in range (0, length):
    print(result[i], end=" ")
