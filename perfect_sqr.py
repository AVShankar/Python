#Given 2 numbers N,M. Print 'yes' if their product is a perfect square else print 'no'

N, M = map(int, input().split())
n = N * M
result=[]
for i in range(1, n+1):
    if(n % i ==0):
        result.append(i)
count = 0
for i in result:
    if(i**2 == n):
        count += 1
        print('yes')
if(count==0):
    print('no')
