#538 - Number made up of two numbers (saturated or unsaturated)

n = input()
n = list(n)
Dict = {}
for i in n:
  if(i not in Dict):
    Dict[i] = 1
  else:
    Dict[i] += 1

if(len(Dict)):
    print('Saturated')
else:
    print('Unsaturated')
