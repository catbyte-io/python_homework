# Task 1: Hello
# Write a function that returns "Hello!"
def hello():
    return "Hello!"

print(hello())

# Task 2: Greet with a Formatted String
# Take one argument and return a greeting "Hello, Name!"
def greet(name):
    return f"Hello, {name}!"

print(greet("Cersei"))

# Task 3: Calculator
# Write a calc function that takes 3 arguments with default thrid argument "multiply"
def calc(num1, num2, operator="multiply"):
    match operator:
        case "add":
            result = num1 + num2
        case "subtract":
            try:
                result = num1 - num2
            except TypeError:
                return "Cannot perform subtraction with strings"
        case "multiply":
            try:
                result = num1 * num2
            except TypeError:
                return "Cannot multiply a string."
        case "divide":
            try:
                result = num1 / num2
            except ZeroDivisionError:
                return "You can't divide by 0!"
