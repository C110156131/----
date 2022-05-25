km = float(input("輸入路程公里數:"))
a = 75
if km <= 1.5:
    print("所需車資為:",a)
elif km > 1.5 and (km-1.5)%0.25 == 0:
    b = (km-1.5)//0.25
    c = 75+5*b
    print("所需車資為:",int(c))
elif km > 1.5 and (km-1.5)%0.25 != 0:
    b = (km-1.5)//0.25
    b+=1
    c = 75+5*b
    print("所需車資為",int(c))