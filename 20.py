s = int(input("輸入組數:"))
a = 0
for i in range(s):
    group = input("全票張數及半票張數:")
    p = group.split(" ")
    price = 250 * int(p[0]) + 175 * int(p[1])
    a += 1
    print("第",a,"組應收費用:",price)