str1 = "紅豆生南國，春來發幾枝?願君多采擷，此物最相思"
str2 = "春眠不覺曉，處處聞啼鳥。夜來風雨聲，花落知多少"
str1.split("，")
str2.split("，")
a = []
for i in str1:
    if i in str2:
        a.append(i)
a.remove("，")
a.remove("，")
print(a)