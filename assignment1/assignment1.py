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
    value_error = f"You can't convert {value} into a {type}."
    match type:
        case "float":
            try:
                converted = float(value)
            except ValueError:
                return value_error
        case "str":
            try:
                converted = str(value)
            except ValueError:
                return value_error
        case "int":
            try:
                converted = int(value)
            except ValueError:
                return value_error
    return converted


# Task 5: Grading System, Using *args
def grade(*args):
    try:
        average = sum(args) / len(args)
    except (TypeError, ZeroDivisionError):
        return "Invalid data was provided."
    if average < 60:
        return "F"
    elif average < 70:
        return "D"
    elif average < 80:
        return "C"
    elif average < 90:
        return "B"
    else:
        return "A"
    

# Task 6: Use a For Loop with a Range
def repeat(string, count):
    word = ''
    for i in range(count):
        word = f"{word}{string}"
    return word


# Task 7: Student Scores, Using **kwargs
def student_scores(choice, **kwargs): 
    match choice:
        case "best":
            # Initialize high_score to keep track of highest score
            high_score = 0

            # Track the highest scoring student
            hs_student = ""

            for student, score in kwargs.items():
                if score > high_score:
                    high_score = score
                    hs_student = student
            return hs_student
        case "mean":
            # Calculate the average of the list of scores
            scores = kwargs.values()
            mean = sum(scores) / len(scores)
            return mean

# Task 8: Titleize, with String and List Operations
def titleize(string):
    # Split the string using whitespace character and assign to a list of words
    words = string.split(' ')

    # Define list of little words to skip capitalization
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]

    # Enumerate the list of words and capitalize the relevant words
    for i, word in enumerate(words):
        # Check if the word is not a little word and if so capitalize
        if words[i] not in little_words:
            # Assign word the new capitalized word
            words[i] = words[i].capitalize()

    # Join the titleized words together using a whitespace character
    new_string = ' '.join(words)

    # Return the new titleized string
    return new_string



### DEBUGGING ###

# Prints "Hello!"
print(hello())

# Prints "Hello, Cersei!"
print(greet("Cersei"))

# Prints "You can't subtract those values!"
print(calc("5", 7, "subtract"))

# Prints "up!up!up!up!up!up!"
print(repeat("up!", 6))

print(titleize("This is a test."))
