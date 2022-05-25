listA = ['飢餓遊戲3','解憂雜貨店','怪獸與他們的產地','哈利波特6','我的阿富汗筆友','祈念之樹','樓下的房客','小王子']
listB = ['房思琪的初戀樂團','等一個人的咖啡','鬼滅之刃14','神農嘗百草','麥田捕手','老人與海','傲慢與偏見','與神同行']
book = str(input("輸入要找的書名:"))
if book in listA:
    a = listA.index(book)
    a+=1
    print("在書架A的第",a,"本")
elif book in listB:
    b = listB.index(book)
    b+=1
    print("在書架B的第",b,"本")
else:
    print("查無此書籍")