#Given a string S, remove the duplicate characters(i.e, characters which repeat) and print the string

N = input()
li=[]

for i in N:
    if i in li:
        continue
    else:
        li.append(i)    

for i in li:
    print(i, end="")
