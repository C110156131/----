s = str(input("輸入一字元為:"))
if s == "".join(reversed(s)):
    print("YES")
else:
    print("NO")