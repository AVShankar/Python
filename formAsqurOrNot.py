#Check whether the given 4 points form a square or not

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
x4, y4 = map(int, input().split())

X = x1 + x2 + x3 + x4
Y = y1 + y2 + y3 + y4

if(X==Y):
  print('yes')
else:
  print('no')
