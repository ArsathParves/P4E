a='I am Arsath Parves'
b=a.split()
print(b)
print(len(b))
print(b[2])

for w in b:
    print (w)

fhand=open('mbox-short.txt')
for line in fhand:
    line=line.rstrip()
    if not line.startswith('From'): continue
    words=line.split()
    email=words[1]
    users=email.split('@')
    print(words[1:2])
    #print (email)
    #print(users)
