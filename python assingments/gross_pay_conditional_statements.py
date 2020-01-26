hrs = input("Enter Hours:")
rpt=input("Enter Rate Per Hours:")
hr=float(hrs)
rph=float(rpt)
# if the hrs value less than 40 below bloch runs's
if hr<=40:
    pay=(hr*rph)
    # If not this block run's
else:
    npay=hr*rph
    xpay=(hr-40.0)*(rph*0.5)
    pay=npay+xpay
    #My 1st logic which is incorrect.
    #xhrs=hr-40
    #xpay=xhrs+rph*0.5
    #pay=xpay+40*rph
print("Pay:",pay)
#xhrs=hrs-40
#hr=float(hrs)
#rph=float(rpt)
#if hr>40 :
#    pay=(hr*rph+(xhrs(rph*1.5)))
#else:
#    pay=(hr*rph)
#print(pay)
