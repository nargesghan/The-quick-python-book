'''If MyError inherits from Exception, what will be the difference between except
Exception as e and except MyError as e?
'''


class MyError(Exception):
    pass

try:
    # Some code that may raise MyError
    raise MyError("Something went wrong")
except MyError as e:
    print(f"Caught MyError: {e}")
except Exception as e2:
    print(f"exception occured{e2}")


try:
    # Some code that may raise MyError
    raise MyError("Something went wrong")
except Exception as e2:
    print(f"exception occured{e2}")

except MyError as e:
    print(f"Caught MyError: {e}")


#The first catches any exception that inherits from Exception (most of them), whereas
#the second catches only MyError exceptions.
