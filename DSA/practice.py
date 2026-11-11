
#Day 1 — Python Basics

#1. Print your details----Print your name, age, and qualification.
'''
name="renu"
age="21"
qualification="B.TECH"
print(f"my name is:{name} my age is:{age} my qulification is:{qualification}")'''

#2. Add two numbers----Take two integers as input and print their sum.
'''
x=int(input("enter a num:"))
y=int(input("enter a num:"))
print(x+y)'''

#3. Arithmetic operations----Take two numbers and print their sum, difference, product, and quotient.

'''x=int(input("enter a num:"))
y=int(input("enter a num:"))
print(x+y)
print(x-y)
print(x*y)
print(x/y)'''

#4. Swap two numbers----Swap the values of two variables.
'''
x=int(input("enter a num:"))
y=int(input("enter a num:"))
print(f"x is {x} y is {y}")
x,y=y,x
print(f"x is {x} y is {y}")
temp=x
x=y
y=temp
print(f"x is {x} y is {y}")
x=x+y
y=x-y
x=x-y
print(f"x is {x} y is {y}")'''

#5. Even or odd using modulo----Take an integer and print its last digit using `%`.

'''num=int(input("enter interger"))
print(num%10)'''

#6. Sum of two digits---Take a two-digit number and calculate the sum of its digits.
'''x=50
sum=0
while 0<x:
    id=x%10
    x=x//10
    sum=sum+id
print(sum)'''

#7. Convert minutes---Convert a given number of minutes into hours and remaining minutes.
'''
min=60
print(min/60)'''

#Day 2 — Conditional Statements

#1. Positive, negative, or zero---Check whether a number is positive, negative, or zero.
'''
num=int(input("enter a num:"))
if num==0:
    print("zero")
elif num<0:
    print("-ve")
else:
    print("+ve")'''

#2.Even or odd---Check whether a number is even or odd.

'''num=int(input("enter a num:"))
if num%2==0:
    print("even")
else:
    print("odd")'''

#3.Largest of two numbers---Take two numbers and print the larger one.
'''
num1=int(input("enter a num:"))
num2=int(input("enter a num:"))
if num1>num2:
    print(num1)
else:
    print(num2)'''

#4.Largest of three numbers---Find the largest of three numbers, including cases where values are equal.

'''
num1=int(input("enter a num:"))
num2=int(input("enter a num:"))
num3=int(input("enter a num:"))
if num1>=num2 and num1>=num3:
    print(num1)
elif num2>=num1 and num2>=num3:
    print(num2)
else:
    print(num3)

    or

if num1>num2:
    if num1>num3:
        print(num1)
    else:
        print(num2)
else:
    if num2>num3:
        print(num2)
    else:
        print(num3)'''

#5. Divisibility check---Check whether a number is divisible by both 3 and 5.
'''
num=int(input("enter a num"))
if num%3==0 and num%5==0:
    print("divisible by both")
else:
    print("not divisible by both")'''

#6.Grade calculator----Input marks and assign grades using your chosen ranges. Handle invalid marks too.
'''marks=int(input("entera num:"))
if marks>100 or marks<0:
    print("enter valid marks")
elif marks>=91:
    print("grad A+")
elif marks>=75:
    print("grad A")
elif marks>=65:
    print("grad B")
elif marks>=45:
    print("grade C")
else:
    print("FAIL")'''

#Day 3 — Loops and Number Logic

#1.Print 1 to N---Take `n` and print every number from 1 to `n`.
'''
n=int(input("enter n value:"))
for i in range(1,n+1):
    print(i)'''
'''
n=int(input("enter n value:"))
i=1
while i<=n:
    print(i)
    i+=1'''

#Sum from 1 to N---Calculate `1 + 2 + ... + n` using a loop.
'''
n=int(input("enter n value:"))
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)

n=int(input("enter n value:"))
i=1
sum=0
while i<=n:
    sum+=i
    i+=1
print(sum)'''

#3. Multiplication table---Print the multiplication table of a given number from 1 to 10.
'''n=int(input("enter n value:"))
for i in range(1,11):
    mul=n*i
    print("{0}*{1} = {2}".format(n,i,mul))'''

'''n=int(input("enter n value:"))
i=1
while i<=10:
    mul=n*i
    print("{0}*{1} = {2}".format(n,i,mul))
    i+=1'''

#4.Count even numbers---Count how many even numbers occur from 1 to `n`.
'''n=int(input("enter n value:"))
count=0
for i in range(1,n+1):
    if i%2==0:
        count+=1
print(count)'''

'''
n=int(input("enter n value:"))
count=0
i=1
while i<=n:
    if i%2==0:
        count+=1
    i+=1
print(count)'''

#5. Sum of even numbers---Find the sum of even numbers from 1 to `n`.
'''n=int(input("enter n value:"))
sum=0
for i in range(1,n+1):
    if i%2==0:
        sum+=i
print(sum)

n=int(input("enter n value:"))
sum=0
i=1
while i<=n:
    if i%2==0:
        sum+=i
    i+=1
print(sum)'''

#6.Reverse a number---Reverse the digits of a positive integer using `%` and `//`.
'''n=int(input("enter n value:"))
rev=0
while 0<n:
    lsn=n%10
    rev=rev*10+lsn
    n=n//10
print(rev)'''

#7.Count digits---Count the number of digits in a positive integer.
'''n=int(input("enter n value:"))
count=0
while 0<n:
    count+=1
    n=n//10
print(count)'''

#Day 4 — Nested Loops and Patterns

#1. Square star pattern---Print a 4 × 4 square of stars.
    
'''for i in range(4):
    for j in range(4):
        print("*",end=" ")
    print()'''

#2.Increasing star triangle---Print 5 rows with 1, 2, 3, 4, and 5 stars.
'''
for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()'''

#3.Repeated-number triangle----Print 1 on row 1, two 2s on row 2, continuing to five 5s.

'''for i in range(1,6):
    for j in range(i):
        print(i,end=" ")
    print()'''
#4.Increasing number triangle----Print rows as `1`, `12`, `123`, `1234`, `12345`.
'''
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()'''
#5.Reverse number triangle---Print rows as `12345`, `1234`, `123`, `12`, `1`.
'''
for i in range(5):
    for j in range(1,6-i):
        print(j,end=" ")
    print()'''

#6.Centered star pyramid---Print 5 centered rows containing 1, 3, 5, 7, and 9 stars.
'''for i in range(5):
    for j in range(4-i):
        print(" ",end="")
    for k in range(2*i+1):
        print("*",end="")
    for l in range(4-i):
        print(" ",end="")
    print()'''
#7.Descending star pyramid---Print 5 rows containing 9, 7, 5, 3, and 1 stars, with leading spaces.
'''for i in range(5):
    for j in range(i):
        print(" ",end="")
    for k in range(9-2*i):
        print("*",end="")
    for l in range(i):
        print(" ",end="")
    print()'''

#Day 5 — Functions and Problem Solving


#1. Square using a function---Write `square(n)` that returns the square of a number.
'''def square(n):
    return n*n
print(square(6))'''

#2. Cube using a function---Write `cube(n)` that returns the cube of a number
'''def cube(n):
    return n*n*n
print(cube(2))'''

#3. Even or odd function---Write `check_even_odd(n)` that returns the result.
'''def check_even_odd(n):
    if n%2==0:
        return "even",n
    else:
        return "odd",n
print(check_even_odd(4))'''

#4. Largest of three---Write `largest(a, b, c)` that returns the largest number, including ties.
'''def largest(a, b, c):
  if a>=b and a>=c:
    return a
  elif b>=a and b>=c:
    return b
  else:
    return c
print(largest(10, 25, 15))'''

#5. Prime number check---Write `is_prime(n)` that returns whether a number is prime. Remember, numbers below 2 are not prime.
'''
def is_prime(n):
  count=0
  for i in range(1,n+1):
    if n%i==0:
      count+=1
  if count==2:
    return "prime"
  else:
    return "not prime"
print(is_prime(7))
print(is_prime(10))
print(is_prime(1))'''

#6. Sum of digits---Write `sum_digits(n)` using a loop.

'''def sum_digits(n):
  sum=0
  while 0<n:
    id=n%10
    sum=sum+id
    n=n//10
  return sum
  
print(sum_digits(26))'''

#7. Count digits---Write `count_digits(n)` using a loop.
'''def count_digits(n):
  count=0
  while 0<n:  
    n=n//10
    count+=1
  return count
print(count_digits(601))'''

#8.Palindrome number---Write `is_palindrome(n)` using number reversal.
'''def is_palindrome(n):
    rev=0
    ov=n
    while 0<n:
        id=n%10
        rev=rev*10+id
        n=n//10
    if ov==rev:
        return "palindrome"
    else:
        return "not palindrome"
print(is_palindrome(120))'''

#1. Create and print a list---Create a list containing 10, 20, 30, 40, 50. Print the entire list.
'''
lst=[10,20,30,40,50]
print(lst)
print(lst[0],lst[2],lst[len(lst)-1])
print(len(lst))
lst[1]=99
print(lst)
lst.append(60)
print(lst)
for i in lst:
    print(i)
sum=0
for i in [10,20,30,40,50]:
    sum=sum+i
print(sum)
count=0
for i in [12,7,8,15,20,3]:
    if i%2==0:
        count+=1
print(count)

lstt=[14,5,28,9,17]
large=lstt[0]
for i in lstt:
    if large<i:
        large=i
print(large)

lst1=[14,5,28,9,17]
larg=lst1[0]
for i in lst1:
    if larg>i:
        larg=i
print(larg)


ls=[1, 2, 3, 4, 5]

for i in range(len(ls)-1,-1,-1):
    print(ls[i])
ls1=[2, 5, 2, 7, 2, 9]
count=0
for i in ls1:
    if i==2:
        count+=1
print(count)

ls2=[10, 5, 20, 8, 20, 15]
lar=ls2[0]
sec=0
for i in ls2:
    if lar<i:
        sec=lar
        lar=i
    elif sec<i and i<lar:
            sec=i
    
print(sec)

    
#4. Separate even and odd numbers----For [1, 2, 3, 4, 5, 6], print the even numbers and odd numbers separately.

for i in [1, 2, 3, 4, 5, 6]:
    if i%2==0:
        print("even num:",i)
    else:
        print("odd num:",i)
#5. Check whether a list is sorted----Return whether [1, 2, 3, 4, 5] is sorted in non-decreasing order. Try another list too.
for i in [1,2,3,4,5]:
    print(i)
'''
'''
ls2 = [10, 10, 8]
lar=ls2[0]
sec=float('-inf')
for i in ls2:
    if lar<i:
        sec=lar
        lar=i
    elif lar>i and sec<i:
        sec=i
print(sec)

ls1=[]
ls2=[]
ls=[1, 2, 3, 4, 5, 6]
for i in range(len(ls)):
    if ls[i]%2==0:
        ls1.append(ls[i])
    else:
        ls2.append(ls[i])
print(ls1)
print(ls2)
count=0
for i in range(1,len(ls)):
    if ls[i-1]>ls[i]:
        count+=1
        break
if count==0:
    print("sorted")
else:
    print(not sorted)



ls2 = [10, 10, 8]
lar=ls2[0]
sec=float('-inf')
for i in ls2:
    if lar<i:
        sec=lar
        lar=i
    elif sec<i and i<lar:
        sec=i
print(sec)
print(lar)'''

#day-7

#List slicing---Print the first three elements, last three elements, and reversed list.


'''
ls=[10,20,30,40,50,60]
print(ls[:3])
print(ls[-1:-4:-1])
print(ls[len(ls)-3::])
print(::-1)
'''
#Insert an element---Insert 25 at index 2 in [10, 20, 30, 40].
'''
ls=[10,20,30,40]
ls.insert(2,25)
print(ls)
'''
#3. Remove duplicates---Create a new list containing only unique elements from [1, 2, 2, 3, 4, 4, 5]. Preserve their original order.
'''
dup=[]
ls=[1,2,2,3,4,4,5]
for i in ls:
    if i not in dup:
        dup.append(i)
print(dup)
'''

#4. Linear search---Search for 30 in [10, 20, 30, 40, 50]. Print its index, or -1 if absent.
'''
ls=[10, 20, 30, 40, 50]
target=30
for i in range(len(ls)):
    if ls[i]==target:
        print(i)
if target not in ls:
        print(-1)
'''
#5. Count occurrences---Count how many times 5 occurs in [5, 2, 5, 7, 5, 9]. Do not use count().
'''
ls=[5, 2, 5, 7, 5, 9]
count=0
for i in ls:
    if i==5:
        count+=1
print(count)
'''
#6. Reverse into a new list---Reverse [1, 2, 3, 4, 5] using a loop and a new empty list.
'''
ls=[1,2,3,4,5]
newls=[]
for i in range(len(ls)-1,-1,-1):
    newls.append(ls[i])
print(newls)
'''
#Find missing number---A list contains numbers from 1 to 5, but one number is missing: [1, 2, 4, 5]. Find it.
'''ls=[1,2,4,5]
for i in range(len(ls)-1):
    if ls[i]+1==ls[i+1]:
        pass
    else:
        print(ls[i]+1)'''
#8. Move zeros to the end---Move all zeros in [0, 1, 0, 3, 12] to the end while preserving the order of nonzero elements.
'''
ls=[0,1,0,3,12]
for i in ls:
    if i==0:
        ls.remove(i)
        ls.append(i)
print(ls)
'''
#9. Binary search---After learning its logic, search for 40 in [10, 20, 30, 40, 50, 60, 70] and return its index.
'''
ls=[10,20,30,40,50,60,70]
l=0
r=len(ls)-1
target=30
while l<=r:
    mid=(r+l)//2
    if target==ls[mid]:
        print("target is found at",mid)
        break
    elif ls[mid]>target:
        l=mid-1
    elif ls[mid]<target:
        r=mid
else:
    print("not found")
    
print("done")'''

'''
ls = [0, 1, 0, 3, 12]
newls=[]
for i in ls:
    if i==0:
        newls.append(i)
        ls.remove(i)
for i in range(newls.count(0)):
    ls.append(0)
print(ls)

ls = [0, 1, 0, 3, 12]
c=ls.count(0)
newls=[]
for i in ls:
    if i!=0:
        newls.append(i)
        
for i in range(c):
    newls.append(0)
print(newls)


ls=[10,20,30,40,50,60,70]
l=0
r=len(ls)-1
target=25
while l<=r:
    mid=(r+l)//2
    if target==ls[mid]:
        print("target is found at",mid)
        break
    elif ls[mid]>target:
        r=mid-1
    elif ls[mid]<target:
        l=mid+1
else:
    print("not found")

'''
#strong number
'''
n=146
n1=n
sum=0
while 0<n:
  fact=1
  id1=n%10
  for i in range(2,id1+1):
    fact=fact*i
  n=n//10
  sum=sum+fact
print(sum)
if sum==n1:
  print("strong")
else:
  print("not")
'''
'''ls=[1,2,4,6,8,9]
for i in range(len(ls)-2):
    if ls[i]+ls[i+1]==10:
        print("two sum ele is:",ls[i],ls[i+1])'''













    
  
