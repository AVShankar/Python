#Given a string and a number K, change every kth character to uppercase from beginning in string

string, K = list(input().split())
K = int(K)
length = len(string)

for i in range (0, length):
    if(K == 0):
        print(string)
        break
    if(i < length-1):
        if((i+1) % K == 0):
            print(string[i].upper(), end="")
        
        else:
            print(string[i].lower(), end="")
        
    else:
        if((i+1) % K == 0):
            print(string[i].upper())
        
        else:
            print(string[i].lower())
