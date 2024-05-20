'''Write code that gets two numbers from the user and divides the first number by the
second. Check for and catch the exception that occurs if the second number is zero
(ZeroDivisionError)'''


try:
    x=int(input())
    y=int(input())
    z=x/y
    print(z)
except ZeroDivisionError:
    print('zero division occured. please try another non-zero numbers')
    x=int(input())
    y=int(input())
    z=x/y
    print(z)
    

  
