#You are given a number ‘n’. You have to tell whether a number is great or not. 
#A great number is a number whose sum of digits let (m) and product of digits let(j) when summed together gives the number back

N = input()
length = len(N)
product = 1
sum = 0
result = 0
for i in range (length):
  product *= int(N[i])
  sum += int(N[i])
result = product + sum
if(result == int(N)):
  print('Great')
else:
  print('no')
