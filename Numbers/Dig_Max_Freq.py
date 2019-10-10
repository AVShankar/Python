#You are given an array of digits. Your task is to print the digit with maximum frequency.
#(596)

N = int(input())
n = list(map(int, input().split()[:N]))

Dict = {}

for i in n:
  if(i not in Dict):
    Dict[i] = 1
  else:
    Dict[i] += 1

for key, value in Dict.items():
  if(value > 1):
    print(key)
    break
