# Given a sentence S of 2 words reverse the order of two words.

S=input()
dividedWord=S.split()
length=len(dividedWord)
if(length <= 10000000):
        for i in reversed(dividedWord):
                print(i, end=" ")
