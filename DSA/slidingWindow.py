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


'''
k=3
ls = [2,1,5,1,3,2]
add=0
for i in range(k):
    add+=ls[i]
t=add
for i in range(len(ls)-k):
    add=add-ls[i]+ls[i+k]
    if add>t:
        t=add
print(t)'''

#Find the length of the smallest subarray whose sum is greater than or equal to a given target.

ls = [2, 3, 1, 2, 4, 3]
target = 7
for i in range(len(ls)):
    

























