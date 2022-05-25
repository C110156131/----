dict1={'金牌':4,'銀牌':5,'銅牌':9,'優牌':7}
list1=[3,1,2,1]
d=input("處理方式(1)字典(2)串列:")
if d=="1":
    item1=dict1.items()
    for x,y in item1:
        print("%s得到%d面"%(x,y))
else:
    print("金牌得%d面"%(list1[0]))
    print("銀牌得%d面"%(list1[1]))
    print("銅牌得%d面"%(list1[2]))
    print("優牌得%d面"%(list1[3]))