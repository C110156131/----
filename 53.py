n = int(input("輸入n值:"))
a = {}
for i in range(0,n):
    name = str(input("請輸入姓名:"))
    mail = str(input("請輸入電子郵件"))
    a[name]=mail
find = str(input("請輸入要查詢電子郵件的姓名:"))
print(a[find])