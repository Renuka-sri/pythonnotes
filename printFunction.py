#print function
sno=28
sname="renu"
ssalary=200000
#print("sno")
#print("sno",sno)
#print(sno,sname,ssalary)
#print(sno,sname,ssalary,sep="@")
#print(sno,sname,ssalary,end='\'')


#formate specifiers
'''
print("sno is:%d"%sno) #int values denoted by %d
print("sno is:%d and s name is:%s"%(sno,sname))# string values ate denoted by %s
avg=19.76548684
print("s avg is:%.2f "%avg)# float values are denoted by %f.
print("s avg is:%.3f "%avg)'''
 #replacement field

print("sno is {} and sname is {}".format(sno,sname))
#manual index
print("sname is {1} and sno is {0}".format(sno,sname))
#manual name based
print("sname is {name} and sno is {n}".format(n=sno,name=sname))

#using f-string
print(f"sname is {sname} and sno is {sno}")

