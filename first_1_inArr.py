#Print the position of first 1 from right to left, in binary representation of an Integer

N = input()
n = list(N)
length = len(n)
rev = reversed(n)
result = list(rev)
for i in range (0, length):
    if(result[i] == '1'):
        print(i+1)
        break
