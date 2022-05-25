while(True):
    s=str(input("檢測的字串(end結束):"))
    a="end"
    if s==a:
        print("檢測結束")
        break
    else:
        b=str(input("檢測的單一字元:"))
        print("字元",b,"出現的次數為:",s.count(b))