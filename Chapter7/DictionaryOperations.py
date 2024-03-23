x = {'a':1, 'b':2, 'c':3, 'd':4}

y = {'a':6, 'e':5, 'f':6}

del x['d'] #x = {'a':1, 'b':2, 'c':3}
print(x,y,sep='/')
print(type(x.setdefault('g', 7)))
z = x.setdefault('g', 7)#z=7 , x= {'a':1, 'b':2, 'c':3,'g':7}
print(x,y,sep="|")
x.update(y)
print(x,y,sep='|')
