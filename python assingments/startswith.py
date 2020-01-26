fhand=open('mypass.txt')
for line in fhand:
    line=line.rstrip()
    if line.startswith("From:"):
        print(line)
