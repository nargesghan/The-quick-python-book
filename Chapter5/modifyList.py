x=[1,2,3,4,5,6,7,8,9,10]
y=x[7:]
x=x[:7]
y.extend(x)
x=y[:] 
#we expect the output of this code to be [8,9,10,1,2,3,4,5,6,7]
print(x)
