# Remove unbalanced paranthesis
# If i/p => (((ab)
# o/p => (ab)

str = input()
leng = len(str)

openB = []
closeB = []
diff = 0 
count = 0
for i in range(0, leng):
    if(str[i] == "("):
        openB.append(i)
        
    elif(str[i] == ")"):
        closeB.append(i)

if(len(openB) > len(closeB)):
    max = "open"
    diff = len(openB) - len(closeB)
    
elif(len(openB) < len(closeB)):
    max = "close"
    diff = len(closeB) - len(openB)
    
if(max == "open"):
    for i in range (0, diff):
        if(count > 1):
            a = str[ :openB[i]-1]
            b = str[ openB[i]: ]
            str = a + b
        else:
            a = str[ :openB[i]]
            b = str[openB[i]+1: ]
            str = a + b
            
if(max == "close"):
    for i in range (0, diff):
        if(count > 1):
            a = str[ :closeB[i]-1]
            b = str[closeB[i]: ]
            str = a + b
        else:
            a = str[ :closeB[i]]
            b = str[closeB[i]+1: ]
            str = a + b

leng =  len(str)
for i in range (0, leng):
    print(str[i], end = "")
