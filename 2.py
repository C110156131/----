s = float(input("輸入一個度數(正整數):"))
a = ""
b = ""
if s <= 120:
    a = s*2.10
    b = s*2.10
elif 120<s<=330:
    a = 120*2.10+(s-120)*3.02
    b = 120*2.10+(s-120)*2.68
elif 330<s<=500:
    a = 120*2.10+210*3.02+(s-330)*4.39
    b = 120*2.10+210*2.68+(s-330)*3.61
elif 500<s<=700:
    a = 120*2.10+210*3.02+170*4.39+(s-500)*4.97
    b = 120*2.10+210*2.68+170*3.61+(s-500)*4.01
else:
    a = 120*2.10+210*3.02+170*4.39+200*4.97+(s-700)*5.63
    b = 120*2.10+210*2.68+170*3.61+200*4.01+(s-700)*4.50
print("Summer months:",'%.2f'%a,",Non Summer months:",'%.2f'%b)
