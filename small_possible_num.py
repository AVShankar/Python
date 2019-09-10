#You are given a number ‘n’. Your task is to create the smallest number possible using the digits of number

N = input()
n = list(N)
length = len(n)
n = sorted(n)
for i in range (0, length-1):
    if(n[i] == '0'):
        n.pop(i)

length = len(n)
for i in range (0, length):
    print(n[i], end="")
