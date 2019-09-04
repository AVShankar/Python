#Find the number of repeated words in a given string

myString=input()
count={}
dividedWord=myString.split(" ")
for i in dividedWord:
        if i in count:
                count[i]+=1
        else:
                count[i]=1
print(count)
