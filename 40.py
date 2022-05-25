n = int(input("輸入整數n:"))

for i in range(1,n,2):
    print(end="    ")
    print(i)
for j in range(1,n+1,2):
    print(j,end="")
for j in range(n-2,0,-2):
    print(j,end="")
print()
for k in range(n-2,0,-2):
    print(end="    ")
    print(k)