s = int(input("輸入金額:"))
a = s//100
b = s%100//50
c = s%50//10
d = s%10//5
e = s%5
total = a+b+c+d+e
print(total)