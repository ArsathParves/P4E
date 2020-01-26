purse= dict()
purse['money']=12
purse['candy']=3
purse['tissues']=75
purse['pen']=2
print(purse)
print(purse['money'])
purse['candy']=purse['candy']+2
print(purse['candy'])


counts=dict()
names=['Arsa','Aswa','Arsa','Nithin','Shanu','Nithin','Big Show','Arsha']
for name in names:
    if name not in counts:
        counts[name]=1
    else:
        counts[name]=counts[name]+1
    print(counts)
