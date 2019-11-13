# First maximum and second minimum and so on
# If i/p => {1, 2, 3, 4, 5, 6, 7}
# o/p => {7, 1, 6, 2, 5, 3, 4}

arr = list(map(int, input().split()))
arr1 = []
arr2 = []

arr.sort()
leng = len(arr)
n = round(leng/2)

for i in range (0, n):
    arr1.append(arr[i])

for i in range (n, leng):
    arr2.append(arr[i])
    
arr2.sort(reverse = True)

count1 = 0
count2 = 0
len1 = len(arr1)
len2 = len(arr2)
for i in range (0, leng):
    if(i %2 == 0):
        if(count2 < len2):
            print(arr2[count2], end=" ")
        
        else:
            print(arr1[count2], end=" ")
        count2 = count2 + 1
    
    else:
        print(arr1[count1], end=" ")
        count1 = count1 + 1
