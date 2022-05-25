n = int(input("輸入一正整數(11<=n<=1000):"))
if n%2==0 and n%11==0 and n%5!=0 and n%7!=0:
    print("Yes")
else:
    print("No")