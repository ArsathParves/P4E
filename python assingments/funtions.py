def computepay():
    try:
        int1 = input("Enter Hours:")
        h = float(int1)
        int2= input("Enter Rate:")
        r = float(int2)
    except:
        print ("Error, please enter a numeric input")
        quit()
    if h >= 40:
        pay1 = 40 * r + (h - 40) * r * 1.5

        return pay1
    else:
        pay2 = h * r
        return pay2
print (computepay())
