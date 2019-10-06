#INPUT: computer program
#OUTPUT: cOMPuteR PROgRaM

s = input().split()
N = len(s)
temp = []
defaultDict = {}
count = 0 
limit = 1

#converting into individual letters
for i in range(N):
    for j in s[i]:
        temp.append(j)

#adding to dict, to find the repetition
for i in temp:
    if(i in defaultDict):
        defaultDict[i] += 1
    else:
        defaultDict[i] = 1

#Making caps for repeated letters
for i in s:
    space = len(i)
    for j in i:
        count += 1
        value = defaultDict[j]
        
        #printing space for next word
        if(count == space):
            if(limit == N):
                if(value > 1):
                    print(j.upper(), end="")
                else:
                    print(j, end="")

            else:
                if(value > 1):
                    print(j.upper(), end=" ")
                else:
                    print(j, end=" ")
                count = 0
        
        else:
            if(value > 1):
                print(j.upper(), end="")
            else:
                print(j, end="")
    limit +=1
