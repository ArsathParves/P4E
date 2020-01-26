#fname = input("Enter file name: ")
#fh = open(fname)
#inp=fh.read()
#ufh=inp.upper()
#sfh=ufh.rstrip()
#print(sfh)
## Read a file and print them the characters in CAPS and strip /n from right of the lines
fname = input("Enter file name: ")
fh = open(fname)
for lx  in fh:
    ly=lx.rstrip()
    print(ly.upper())
