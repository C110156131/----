a=str(input("輸入一整數數列"))
aa=a.split(" ")
for i in range(0,len(aa)):
    if int(aa.count(aa[i]))>len(aa)/2:
        a=int(aa[i])
        print("過半元素為:",a)
        break
    else:
        print("過半元素為:NO")
        break