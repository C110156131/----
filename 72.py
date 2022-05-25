n = int(input("n支紙菸:"))
k = int(input("k支菸屁股合成一支紙菸:"))
while k>1:
    a = n//k
    b = (n%k+a)//k
    n = n+a+b
    break
print("可以抽",n,"支紙菸")