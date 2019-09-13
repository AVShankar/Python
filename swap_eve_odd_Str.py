#Given a string s swap the even and odd characters.Assume the index starts from 0

n = input()
N = list(n)
length = len(N)
for i in range (0, length, 2):
    if(i == length-1):
        break
    
    else: 
        temp = N[i]
        N[i] = N[i+1]
        N[i+1] = temp

for i in range (0, length):
    print(N[i], end="")
