# Radha newly learnt about palindromic strings.
#A palindromic string is a string which is same when read from left to right and also from right to left.
#Help her in implementing the logic


s = input()
temp = []
s= list(s)
for i in reversed(s):
    temp.append(i)
if(s == temp):
    print(1)
else:
    print(0)
