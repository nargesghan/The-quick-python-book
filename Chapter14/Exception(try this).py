'''What code would you use to create a custom ValueTooLarge exception and raise that
exception if the variable x is over 1000?
'''
class ValueTooLarge(Exception):
    pass

x=200
if x>1000:
    raise ValueTooLarge()