#Write a program which displays whether the given two strings are complementary or not. 
#Assume both the string contains unique capital alphabets in alphabetical order. 
#Their total length has to be 26. If we join alphabets of both the strings we should get all capital letters exactly once, 
#then only we can call them as complementary. Print complementary/non-complementary

list1 = input()
list2 = input()
list1 = list(list1)
list2 = list(list2)
defaultList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

checkList = list1 + list2

checkList.sort()
if(checkList == defaultList):
    print("complementary")
else:
    print("non-complementary")
