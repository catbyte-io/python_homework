# Task 2: A Decorator that Takes an Argument
def type_converter(type_of_output):
    def type_decorator(func):
        def wrapper(*args, **kwargs):
            x = func(*args, **kwargs)
            return type_of_output(x)
        return wrapper
    return type_decorator


# Converts 5 to a string
@type_converter(str)
def return_int():
    return 5


# Attempts to convert a non number string to an int and fails
@type_converter(int)
def return_string():
    return "not a number"


y = return_int()
print(type(y).__name__)
try:
    y = return_string()
    print("shouldn't get here!")
except ValueError:
    print("can't convert that string to an integer!")  # We should get here
