#1021
'''
s = "(()())(())"
emp=""
count=0
for i in s:
    if i=="(":
        count+=1
        if count>1:
            emp+=i
    else:
        if i==')':
            count-=1
            if count>=1:
                emp+=i
print(emp)'''

#1614
'''
s = "(1+(2*3)+(((8))))"
count=0
maxcount=0
for i in s:
    if i=="(" or i==")":
        if i=="(":
            count+=1
            if count>maxcount:
                maxcount=count
        else:
            if i==")":
                count-=1
        
    else:
        pass
print(maxcount)'''

#13 roman interget
dic={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
s="CDXLIV"
add=0
i=1
while i<len(s):
    if dic[s[i]]<=dic[s[i-1]]:
        add+=dic[s[i-1]]
        i+=1
    else:
        add+=dic[s[i]]-dic[s[i-1]]
        i+=2
if len(s)==i:
    add+=dic[s[len(s)-1]]
print(add)
    



























            
