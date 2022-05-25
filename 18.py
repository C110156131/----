card = str(input("輸入五張牌(包含A,J,Q,K):"))
card1 = card.split(",")
total = 0
for i in range(len(card1)):
    if str(card1[i]) == "A":
        total += 1
    elif str(card1[i]) == "J":
        total += 11
    elif str(card1[i]) == "Q":
        total += 12
    elif str(card1[i]) == "K":
        total += 13
    else:
        total += int(card1[i])
print(total)