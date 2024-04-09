'''What would be the result of changing a list or dictionary that was passed into a function
as a parameter value? Which operations would be likely to create changes that would be
visible outside the function? What steps might you take to minimize that risk?
'''
def func( dict):
    dict.setdefault('Hello', 'Narges')
    print(dict)

dict={1:'one'}
func(dict)
print(dict)


'''In Python, lists and dictionaries are mutable data types.
 This means that if you pass a list or a dictionary into a function and modify it within the function,
  the changes will be visible outside the function as well.
  This is because the function is working with a reference to the original object, not a copy of it.'''

'''To minimize the risk of unintentionally modifying the original list or dictionary,
   you can create a copy of the object at the beginning of the function.
    You can do this using the copy method for lists and the copy method or dict function for dictionaries.'''

def safe_modify_dict(dict):
    dict = dict.copy()
    dict['new item']='new item'
    print(dict)


safe_modify_dict(dict)
print(dict)  
