#using two pointers and sliding window
#reverse
'''ls=[10,20,30,40,50]
l=0
r=len(ls)-1
while l<r:
    ls[l],ls[r]=ls[r],ls[l]
    l+=1
    r-=1
print(ls)'''

#palindrome
'''s="madam"
l=0
count=0
r=len(s)-1
while l<r:
    if s[l]!=s[r]:
       count+=1
       break
    r-=1
    l+=1
if count:
    print("not palindrome")
else:
    print("palindrome")
s="madam"
l=0
r=len(s)-1
while l<r:
    if s[l]!=s[r]:
       print("not palindrome")
       break
    r-=1
    l+=1
else:
    print("palindrome")'''
'''
ls=[1,2,4,6,8,19]
t=10
l=0
r=len(ls)-1
sum1=0
while l<r:
    sum1=ls[l]+ls[r]
    if sum1==t:
        print("",ls[l],ls[r])
        break
    elif sum1<t:
        l+=1
    elif sum1>t:
        r-=1

ls = [0, 1, 0, 3, 12]
l=0
r=0
while l<len(ls):
    if ls[l]!=0:
        ls[r],ls[l]=ls[l],ls[r]
        r+=1
    l+=1
print(ls)'''

#remove duplicates from the shorted array.
'''ls=[10,20,20,39,39,60,60]
r=0
l=1
while l<len(ls):
    if ls[r]==ls[l]:
        ls.remove(ls[l])
    else:
        r+=1
        l+=1
print(ls)'''

'''ls = [10, 20, 20, 39, 39, 60, 60]

r = 0
l = 1

while l < len(ls):
    if ls[r] != ls[l]:
        r += 1
        ls[r] = ls[l]
    l += 1

print(ls[:r+1])'''


#check palindrome or not
'''s = "A man, a plan, a canal: Panama"
l=0
r=len(s)-1
while l<r:
    if not s[l].isalnum():
        l+=1
        continue
    if not s[r].isalnum():
        r-=1
        continue
    if s[l].lower()!=s[r].lower():
            print("False")
            break
            
    l+=1
    r-=1
else:
    print("True")
'''
#Given an array, find the maximum sum of any 3 consecutive elements.
'''
ls=[2,1,5,1,3,2]
t=0
for i in range(len(ls)-2):
    add=ls[i]+ls[i+1]+ls[i+2]
    if add>t:
        t=add
print(t)'''


'''ls=[2,1,5,1,3,2,9]
t=0
add=ls[0]+ls[1]+ls[2]
for i in range(len(ls)-3):
    add=add-ls[i]+ls[i+3]
    if add>t:
        t=add
print(t)'''

'''
ls = [4, 2, 10, 3, 8, 1, 5]
add=ls[0]+ls[1]+ls[2]+ls[3]
t=add
for i in range(len(ls)-4):
    add=add-ls[i]+ls[i+4]
    if add>t:
        t=add
print(t)'''
'''
ls = [4, 2, 10, 3, 8, 1, 5]
add=ls[0]+ls[1]+ls[2]
t=add
for i in range(len(ls)-3):
    add=add-ls[i]+ls[i+3]
    if add<t:
        t=add
print(t)'''
    
#Find the maximum average of any 5 consecutive elements.
'''ls = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5
sw=ls[0]+ls[1]+ls[2]+ls[3]+ls[4]
avg=sw/k
for i in range(len(ls)-k):
    sw=sw-ls[i]+ls[i+5]
    preavg=sw/k
    if preavg>avg:
        avg=preavg
print(avg)'''

k=3
ls = [2,1,5,1,3,2]
add=0
for i in range(k):
    add+=ls[i]
t=add
for i in range(len(ls)-3):
    add=add-ls[i]+ls[i+3]
    if add>t:
        t=add
print(t)













































































