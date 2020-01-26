# Simple text file line count program
# fhand(is the handler)
#open(inbuilf function to open the text)
#count (inbuilf function to Count)
fhand=open('mypass.txt')
count=0
for line in fhand:
    count=count+1
print('Line Count:',count)
