from posixpath import split


sA = str(input("輸入字串sA:"))
sB = str(input("輸入字串sB:"))
if sA in sB:
    print("YES")
else:
    print("NO")