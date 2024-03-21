x="{1:{0}}".format(3,4)
print(x)#  4
x="{0:$>5}".format(3)
print(x)#$$$$3
x="{a:{b}}".format(a=1,b=5)
print(x)#    1
x="{a:{b}}:{0:$>5}".format(3,4,a=1,b=5,c=10)
print(x)#   1:$$$$3