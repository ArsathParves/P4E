x=input("Enter the vaule of x:",)
y=input("Enter the value of y:",)
z=input("Enter the value of z:",)

def greater():
    if x<y:
        print("Big Number",x)
        print ("Small Number",y)
    else:
        print("Big Number",y)
        print ("Small Number",x)
greater()

def three_greater(x,y,z):
    return greater(x,greater(y,z))
three_greater()
