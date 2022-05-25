a = list(input("請輸入第一組數字:"))
b = list(input("請輸入第二組數字:"))
A = B = 0
if a == b:
    print("4A0B","全對")
else:
    for i in range(len(a)):
        if a[i] == b[i]:
            A+=1
        elif a[i]!=b[i] and a.count(b[i])>0:
            B+=1
    print(A,"A",B,"B","加油")