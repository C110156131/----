N = str(input("輸入0~9的數字所組成的N個數字字串(1<=N<=7):"))
N.split(",")
Max = sorted(N,reverse=True)
min = sorted(N)
Max1 = ""
min1 = ""
for i in range(0,len(N)):
    Max1 += Max[i]
    min1 += min[i]
s = int(Max1) - int(min1)
print(s)