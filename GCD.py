#Given 2 numbers N,M. Find the GCD

N, M = map(int, input().split())
result1 = []
result2 = []
for i in range(1, N + 1):
       if N % i == 0:
           result1.append (i)

for i in range(1, M + 1):
       if M % i == 0:
           result2.append (i)

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

intercept = intersection(result1, result2)
final = 1
for i in intercept:
    final = final * i

print(final)
