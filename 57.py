combo = str(input("請選擇主餐及升級的套餐:"))
combo.split(",")
updrink = str(input("是否升級成大杯飲料:"))
upfood = str(input("是否換成大薯:"))
if combo[0] == "1":
    money = 72
elif combo[0] == "2":
    money = 62
elif combo[0] == "3":
    money = 82
elif combo[0] == "4":
    money = 44
elif combo[0] == "5":
    money = 60
if combo[1] == "A":
    money1 = 55
elif combo[1] == "B":
    money1 = 68
if updrink == "是":
    money2 = 7
elif updrink == "否":
    money2 = 0
if upfood == "是":
    money3 = 13
elif upfood == "否":
    money3 = 0
total = money+money1+money2+money3
print("總共為",total,"元")