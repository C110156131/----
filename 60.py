english = str(input("輸入一小串小寫英文:"))
transTable = english.maketrans("aeiou", ".....")
s = english.translate(transTable)
print(s)