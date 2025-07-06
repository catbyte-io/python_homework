# Task 1: Hello
# Write a function that returns "Hello!"
def hello():
    return "Hello!"


# Task 2: Greet with a Formatted String
# Take one argument and return a greeting "Hello, Name!"
def greet(name):
    return f"Hello, {name}!"


# Task 3: Calculator
# Write a calc function that takes 3 arguments with default thrid argument "multiply"
def calc(num1, num2, operator="multiply"):
    type_error = f"You can't {operator} those values!"
    zero_error = "You can't divide by 0!"

    match operator:
        case "add":
            try:
                result = num1 + num2
            except TypeError:
                return type_error
        case "subtract":
            try:
                result = num1 - num2
            except TypeError:
                return type_error
        case "multiply":
            try:
                result = num1 * num2
            except TypeError:
                return type_error
        case "divide":
            try:
                result = num1 / num2
            except TypeError:
                return type_error
            except ZeroDivisionError:
                return zero_error
        case "modulo":
            try:
                result = num1 % num2
            except TypeError:
                return type_error
            except ZeroDivisionError:
                return zero_error
        case "int_divide":
            try:
                result = num1 // num2
            except TypeError:
                return type_error
        case "power":
            try:
                result = num1 ** num2
            except TypeError:
                return type_error
        # Default case to catch all other arguments
        case _:
            return "Please choose from the following: add, subtract, multiply, divide, modulo, int_divide, or power."
    return result


# Task 4: Data Type Conversion
# Create a function that takes two parameters: a value and the type to convert to
def data_type_conversion(value, type):
    type_error = f"You can't convert {value} into a {type}."
    

### DEBUGGING ###

# Prints "Hello!"
print(hello())

# Prints "Hello, Cersei!"
print(greet("Cersei"))

# Returns "You can't subtract those values!"
print(calc("5", 7, "subtract"))

