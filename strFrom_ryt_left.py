#Print the string from characters right to left (With first letter Caps)


s = input()
arr = list(s)
count = 0
for i in reversed(arr):
    if(count == 0):
        print(i.upper(), end="")
    else:
        print(i, end="")
    count +=1
