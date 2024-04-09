
'''
How would you write a function that could take any number of unnamed arguments
and print their values out in reverse order?'''

def func(*args):
    for arg in args[-1::-1]:
        print(arg)

func(1,2,3,4,5,6,7)


'''
What do you need to do to create a procedure or void function—that is, a function with
no return value?'''

#I just don't use return expression in my function. then by default it returns none value

'''What happens if you capture the return value of a function with a variable?
'''
