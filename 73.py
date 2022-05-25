time1 = str(input("輸入時間1(時、分、秒):"))
time2 = str(input("輸入時間2(秒):"))
s = time1.split(":")
tran1 = int(s[0])*60*60+int(s[1])*60+int(s[2])
tran21 = int(time2)//3600
tran22 = int(time2)%3600//60
tran23 = int(time2)%3600%60
print("時間1(",time1,")格式轉換後為",tran1,"秒")
print("時間2(",time2,"秒)=",tran21,":",tran22,":",tran23)