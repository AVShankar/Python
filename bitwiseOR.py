#Given a number N and an array of N integers, find the Bitwise OR of the array

def bitOr(arr, N):
  result = arr[0]
  for i in range (1, N):
    result |= arr[i]
  return result

N = int(input())
arr = list(map(int, input().split()[:N]))
print(bitOr(arr, N))
