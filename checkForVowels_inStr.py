#Given a number N and an array of N strings,Print yes, if all strings have atleast one vowel in them otherwise print no

N = int(input())
s = []
count = 0
for i in range (0, N):
    c = input()
    s.append(c)

for i in s:
    arr = list(i)
    for j in arr:
        if(j == 'a' or j == 'e' or j == 'i' or j == 'o' or j == 'u' or j == 'A' or j == 'E' or j == 'I' or j == 'O' or j == 'U'):
            count += 1 
            break

if(count == N):
    print("yes")
else:
    print("no")
