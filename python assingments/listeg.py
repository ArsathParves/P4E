friends=['Arsath','Nithin','Shanu','Abishek']

#Loop between list elements
for friend in friends:
    print('Happy New year -_-',friend)

#Lenght of the list
for i in range(len(friends)):
    friend= friends[i]
    print(i)

#Adding list  or concatinate them
a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)

# Slicing list
print(a[1:3])
print(b[:2])
print(c[5:])

# Appending list
things=list()
things.append('Stone')
print(things)
things.append('House')
print(things)

#Sorting list
friends.sort()
print(friends)
