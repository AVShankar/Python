#Given a number N print a right angled traingle structure with the starting level as single 1 and every immediate 
#proceeding level with 2 more additional ones than the previous level
#Repeat the pattern for N levels

N = int(input())
count = 1
if(N <= 1000):
    for i in range (0, N):
        for j in range (0, count): #3
            if(j < count-1):
                print(1, end = " ")
            else:
                print(1)
        count += 2
