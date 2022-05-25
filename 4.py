x = int(input("輸入x軸座標:"))
y = int(input("輸入y軸座標:"))
a = ""
if x>0 and y>0:
    a = x**2 + y**2
    print("該點位於第一象限,離原點距離為根號%d"%(a))
elif x<0 and y>0:
    a = abs(x)**2 + y**2
    print("該點位於第二象限,離原點距離為根號%d"%(a))
elif x<0 and y<0:
    a = abs(x)**2 + abs(y)**2
    print("該點位於第三象限,離原點距離為根號%d"%(a))
elif x>0 and y<0:
    a = x**2 + abs(y)**2
    print("該點位於第四象限,離原點距離為根號%d"%(a))
elif x==0 and y>0:
    a = y
    print("該點位於上半平面Y軸上,離原點距離為%d"%(a))
elif x==0 and y<0:
    a = abs(y)
    print("該點位於下半平面Y軸上,離原點距離為%d"%(a))
elif x>0 and y==0:
    a = x
    print("該點位於右半平面X軸上,離原點距離為%d"%(a))
elif x<0 and y==0:
    a = abs(x)
    print("該點位於左半平面X軸上,離原點距離為%d"%(a))
elif x==0 and y==0:
    print("該點位於原點")