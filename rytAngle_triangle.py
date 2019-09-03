A, B, C = map(int,input().split())
if(A<=10000 and B<=10000 and C<=10000):
    if(A>0 and B>0 and C>0):
        if(A+B>C):
            if(A*A + B*B == C*C):
                print("yes")
            else:
                print("no")
        else:
            print("no")
    else:
        print("no")
else:
    print("no")
