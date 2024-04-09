'''What would you need to modify in the previous code for the function four()to make it
work for any number? What would you need to add to allow the starting point to also be
set?'''


'''>>> def four():
... x = 0 1
... while x < 4:
... print("in generator, x =", x)
... yield x 2
... x += 1 '''

def four(x):
    i=0
    while i<x:
        print("in generator, i =", i)
        yield i
        i=i+1

for i in four(6):
    pass


#To specify the start:
def four1(start, end):
    i=start
    while i<end:
        print("in generator, i =", i)
        yield i
        i=i+1


for i in four1(3,6):
    pass