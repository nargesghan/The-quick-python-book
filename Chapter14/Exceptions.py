'''Do Python exceptions force a program to halt?
Suppose that you want accessing a dictionary x to always return None if a key doesn’t
exist in the dictionary (that is, if a KeyError exception is raised). What code would you
use?'''


'''
Python exceptions do not necessarily force a program to halt. When an exception is raised, it can be caught and handled using a try-except block. If the exception is handled, the program can continue running.'''


dict={'1':'one','2':'two','3':"three"}

try:
    x=input("key: ")
    print(dict[x])
except KeyError as err:
    print(f'{err} has been occured')


#Alternative Approach Using dict.get()
