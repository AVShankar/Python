#Print next date from the given date

date = list(map(int, input().split(",")))

temp = date

if(date[1] == 1 or date[1] == 3 or date[1] == 5 or date[1] == 7 or date[1] == 8 or date[1] == 10):
    if(date[0] == 31):
        temp[0] = 1
        temp[1] = temp[1] + 1
    
    else:
        temp[0] = temp[0] +1

if(date[1] == 2 or date[1] == 4 or date[1] == 6 or date[1] == 9 or date[1] == 11):
    if(date[0] == 30):
        temp[0] = 1
        temp[1] = temp[1] + 1

    else:
        temp[0] = temp[0] + 1

if(date[1] == 12):
    if(date[0] == 31):
        temp[0] = 1
        temp[1] = 1
        temp[2] = temp[2] + 1


for i in range (0, 3):
    if(i<2):
        print(temp[i], end=",")
    else:
        print(temp[i])
