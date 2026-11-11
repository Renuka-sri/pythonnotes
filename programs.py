
#accept two num from user and add two num(+)
'''
a=int(input("enter a value:"))
b=int(input("enter b vale:"))
print("addition of two num:",a+b)
print("================================================")
'''
#accept two num from user and sub(-)
'''
a=int(input("enter a value:"))
b=int(input("enter b vale:"))
print("subtraction of two num:",a-b)
print("================================================")
'''
#accept two num from user and mul(*)
'''
a=int(input("enter a value:"))
b=int(input("enter b vale:"))
print("multiplication of two num:",a*b)
print("================================================")
'''

#accept two num from user and (/)
'''
a=int(input("enter a value:"))
b=int(input("enter b vale:"))
print("division of two num:",a/b)
print("================================================")'''

#accept two num from user and  do (%)
'''
a=int(input("enter a value:"))
b=int(input("enter b vale:"))
print("modulas of two num:",a%b)
print("================================================")'''

#accept two num from user and  do (//)"
'''
a=int(input("enter a value:"))
b=int(input("enter b vale:"))
print("floor division of two num:",a//b)
print("================================================")'''

#accept two num from user and  do (**)
'''
a=int(input("enter a value:"))
b=int(input("enter b vale:"))
print(f"{a}power of {b} is:",a**b)
print("================================================")'''

#accept present reading and previous reading calculate no.of units and find biil.
'''
prr=int(input("enter present reding"))
pvr=int(input("enter previous reading"))
nounits=pvr-prr
bill=nounits*2
print("no.of units",nounits)
print("bill is",bill)'''


#area of a triangle
'''
h=int(input("enter h value:"))
b=int(input("enter b vale:"))
area=0.5*h*b;
print("area of  triangle is:",area)'''

#area of a rect
'''
l=int(input("enter l value:"))
b=int(input("enter b vale:"))
area=l*b;
print("area of  rect is:",area)
'''
#area of a circle
'''
r=int(input("enter r value:"))
area=3.14*r*r
print("area of  circle is:",area)'''

#circumstance of circle
'''
r=int(input("enter r value:"))
area=2*3.14*r
print(" circumstance of  circle is:",area)'''


#find greatest of 4 numbers.
'''
num1=int(input("enter a numbber:"))
num2=int(input("enter a numbber:"))
num3=int(input("enter a numbber:"))
num4=int(input("enter a numbber:"))

if num1>num2:
    if num1>num3 and num1>num4:
        print(num1)
    else:
        if num3>num4:
            print(num3)
        else:
            print(num4)
else:
    if num2>num3 and num2>num4:
        print(num2)
    else:
        if num3>num4:
            print(num3)
        else:
            print(num4)
    
if num1>num2 and num1>num3 and num1>num4:
    print(num1,"is big")
elif num2>num1 and num2>num3 and num2>num4:
    print(num2,"is big")
elif num3>num2 and num3>num1 and num3>num4:
    print(num3,"is big")
else:
    print(num4,"is big")'''



#accept the age from the user and print child,teen,middle,old age based on conditiions
'''
age=int(input("enter the age:"))
if age<=5:
    print("kid")
elif age>=6 and age<=12:
    print("child")
elif age>=13 and age<=19:
    print("teen")
elif age>=20 and age<=50:
    print("mid")
else:
    print("old age")

if age<=5:
    print("kid")
elif age<=12:
    print("child")
elif age<=19:
    print("teen")
elif age<=50:
    print("middle")
else:
    print("oldage")
'''

#atm
'''
oldbal=float(input("enter your old balance:"))
ttype=input("enter your transaction type:(w/d)")
tamt=float(input("enter your transaction amount:"))

if ttype in "wW":
    if tamt>oldbal:
        print("insuficient fund")
    else:
        if tamt==oldbal:
            print("please mintain minimum balance")
        else:
            cbal=oldbal-tamt
            print("current balance",cbal)
elif ttype in "dD" :
    if tamt>=50000:
        print("required pin")
    else:
        cbal=oldbal+tamt
        print("current balance",cbal)
else:
    print("invalid transaction type")'''



















