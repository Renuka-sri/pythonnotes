#int()
'''
x=12.2
y=int(x)
print(type(x),">>>>>>>",type(y))
print("result is",y)
x="123"
y=int(x)
print(type(x),">>>>>>>",type(y))
print("result is",y)
x=True
y=int(x)
print(type(x),">>>>>>>",type(y))
print("result is",y)
x=20+10j
y=int(x)
print(type(x),">>>>>>>",type(y))
print("result is",y)#type error'''


#float
'''
x=12
y=float(x)
print(type(x),">>>>>>>",type(y))
print("result is",y)
x="123"
y=float(x)
print(type(x),">>>>>>>",type(y))
print("result is",y)
x=False
y=float(x)
print(type(x),">>>>>>>",type(y))
print("result is",y)
x=10+20j
y=float(x)
print(type(x),">>>>>>>",type(y))
print("result is",y)#type error'''


#srt()
'''
x=123
y=str(x)
print(type(x),">>>>>>>",type(y))
print("result is",y)
x=12.2
y=str(x)
print(type(x),">>>>>>>",type(y))
print("result is",y)
x=False
y=str(x)
print(type(x),">>>>>>>",type(y))
print("result is",y)
x=10+20j
y=str(x)
print(type(x),">>>>>>>",type(y))
print("result is",y)'''

#bool()
'''
x=12
y=bool(x)
print(type(x),">>>>>>>",type(y))
print("result is",y)
x=12.3
y=bool(x)
print(type(x),">>>>>>>",type(y))
print("result is",y)
x="string"
y=bool(x)
print(type(x),">>>>>>>",type(y))
print("result is",y)
x=10+20j
y=bool(x)
print(type(x),">>>>>>>",type(y))
print("result is",y)
x=""
y=bool(x)
print("result is",y)
x=" "
y=bool(x)
print("result is",y)
x=0
y=bool(x)
print("result is",y)
x=0.0
y=bool(x)
print("result is",y)
x=0+0j
y=bool(x)
print("result is",y)
x=0.0+0.0j
y=bool(x)
print("result is",y)
x=None
y=bool(x)
print("result is",y)
x=[]
y=bool(x)
print("result is",y)
x=()
y=bool(x)
print("result is",y)
x=0j
y=bool(x)
print("result is",y)
x=set()
y=bool(x)
print("result is",y)
x={}
y=bool(x)
print("result is",y)'''

#complex(x) when we have only one value x-real value
'''
x =12
y =complex(x)
print(type(x),">>>>>>>",type(y))
print("result is",y)
x =12.0
y =complex(x)
print(type(x),">>>>>>>",type(y))
print("result is",y)
x ="12"
y =complex(x)#value error(if we use " char")
print(type(x),">>>>>>>",type(y))
print("result is",y)
x =True
y =complex(x)
print(type(x),">>>>>>>",type(y))
print("result is",y)'''

#complex(x,y) when we have two  values x-real value| y- img value
'''
x=12
y=10
z=complex(x,y)
print(type(x),type(y),">>>>>>>",type(z))
print("result is",z)
x=12.5
y=10.3
z=complex(x,y)
print(type(x),type(y),">>>>>>>",type(z))
print("result is",z)
x="12"
y="10"
z=complex(x,y) #TypeError: complex() can't take second arg if first is a string
print(type(x),type(y),">>>>>>>",type(z))
print("result is",z)
x=True
y=False
z=complex(x,y)
print(type(x),type(y),">>>>>>>",type(z))
print("result is",z)'''


















