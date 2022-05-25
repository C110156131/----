m = int(input("輸入階層值M:"))
N = 1
n = 1
a = 0
while N<m:
    N=N*n
    n+=1
    a+=1
print("超過M為",m,"的最小階層N值為:",a)