#You are given a number ‘n’.Your task is to develop an algorithm to tell 
#whether the number is ‘ajs’ or not.An ‘ajs’ number is a number whose sum of first two digits is present in given number ‘n’
# (544)

n = input()

sum = int(n[0]) + int(n[1])

if(str(sum) in n):
  print('1')
else:
  print('0')
