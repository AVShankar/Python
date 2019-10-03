#Given a number 'N' print the sum of each digit to the power of number of digits in given input

N = input()
arr = list(N)
result = 0
print(arr)

length = len(arr)

for i in arr:
    i = int(i)
    result += i**length

print(result)
