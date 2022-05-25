all = ['John','Mary','Tina','Fiona','Clair','Eva','Ben','Bill','Bert']
Englishpass = ['John','Mary','Fiona','Clair','Ben','Bill']
mathpass = ['Mary','Fiona','Clair','Eva','Ben']
a = []
b = []
c = []
a = set(Englishpass)&set(mathpass)
b = set(all)-set(mathpass)
c = set(all)-set(mathpass)&set(Englishpass)
print(a)
print(b)
print(c)