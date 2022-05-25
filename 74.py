list1=['red','blue','red','green']
n=1
while n<11:
    color=str(input("依序輸入四個顏色(以空白間隔):"))
    n+=1
    if n==11 and color!="red blue red green":
        print("挑戰失敗")
        break
    else:
        if color=="red blue red green":
            print("挑戰成功")
        else:
            s=""
            a=color.split(" ")
            for i in range(0,4):
                if a[i]==list1[i]:
                    s+="1"
                elif a[i]!=list1[i] and list1.count(a[i])>0:
                    s+="2"
                else:
                    s+="3"
            print(s)