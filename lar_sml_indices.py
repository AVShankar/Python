#Given a number N followed by N numbers. Find the smallest number and largest number and print both the indices(1based indexing)

N=int(input())
K=list(map(int, input().split()[:N]))
temp = sorted(K)
print(K.index(temp[0])+1, K.index(temp[-1])+1)
