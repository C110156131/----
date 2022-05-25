s = int(input("輸入西元年:"))
list1 = ['鼠','牛','虎','兔','龍','蛇','馬','羊','猴','雞','狗','豬']
if s%12==4:
    print(list1[0])
elif s%12==5:
    print(list1[1])
elif s%12==6:
    print(list1[2])
elif s%12==7:
    print(list1[3])
elif s%12==8:
    print(list1[4])
elif s%12==9:
    print(list1[5])
elif s%12==10:
    print(list1[6])
elif s%12==11:
    print(list1[7])
elif s%12==0:
    print(list1[8])
elif s%12==1:
    print(list1[9])
elif s%12==2:
    print(list1[10])
elif s%12==3:
    print(list1[11])