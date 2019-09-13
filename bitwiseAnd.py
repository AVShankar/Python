#Given a number N and an array of N integers, find the Bitwise AND of the array

def bitAnd(arr, n): 
    ans = arr[0] 
    for i in range(1, N): 
        ans &= arr[i] 
        # print(i)          
    return ans

N = int(input())
arr = list(map(int, input().split()[:N]))
print(bitAnd(arr, N))
