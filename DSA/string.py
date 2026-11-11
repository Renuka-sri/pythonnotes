
#Problem 1 – Count characters---Write a Python program to count the number of characters in a string without using len().
'''
s="python"
count=0
for _ in s:
    count+=1
print(count)'''

#Problem 2 – Reverse a string---Reverse the given string without using slicing ([::-1]).
'''
s="hello"
for i in range(-1,-6,-1):
    print(s[i],end="")'''

#Problem 3 – Count vowels---Count how many vowels (a, e, i, o, u) are present in a string.
'''
s = "education"
ls=['a','e','i','o','u']
count=0
for i in s:
    if i in ls:
        count+=1
print(count)'''

#Problem 4 – Count uppercase and lowercase letters
'''
s = "PyThOn"
count1=0
count2=0
for i in s:
    if i.isupper():
        count1+=1
    if i.islower():
        count2+=1
print("upper:",count1)
print("lower:",count2)'''

#Problem 5 – Palindrome string---Check whether a string reads the same forward and backward.
'''
s = "madam"
sr=s[::-1]
if s==sr:
    print("palindrome")
else:
    print("not a palindrome")

s = "madam"
srt=""
for i in range(-1,-6,-1):
    srt=srt+s[i]
if s==srt:
    print("palindrome")
else:
    print("not a palindrome")'''

#Problem 6 – Count a particular character---Count how many times "a" appears.
'''
s = "banana"
target = "a"
count=0
for i in s:
    if target==i:
        count+=1
print(count)

print(s.count('a'))'''

#Problem 7 – Remove duplicate characters---Given a string, remove duplicate characters while preserving their original order.
'''
s = "programming"
ls=""
for i in s:
    if i in ls:
        pass
    else:
        ls+=i
print(ls)'''
    
#Problem 8 – Find the first non-repeating character
'''
s = "swiss"
for i in s:
    if s.count(i)>1:
       pass
    else:
        print(i)
        break

s = "swiss"
dic={}
for i in s:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
for j in dic:
    if dic[j]==1:
        print(j)
        break '''

#Problem 9 – Character frequency---Count how many times each character occurs.
'''
dic={}
s = "banana"
for i in s:
    if i in dic:
        dic[i]+=1 #increase the value by one.
    else:
        #use it as the key.
        dic[i]=1
print(dic)'''

#Problem 10---Find the first repeating character in a string.
'''
s = "programming"
dic={}
for i in s:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
for j in dic:
    if dic[j]>1:
        print(j)
        break
'''















