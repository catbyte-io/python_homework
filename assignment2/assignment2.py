import os
import csv
import traceback
import custom_module
from datetime import datetime


# Helper function to print stack trace for exceptions
def print_stack_trace(e):
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
            print(f"Exception type: {type(e)._name_}")
            message = str(e)
            if message:
                print(f"Exception message: {message}")
            print(f"Stack trace: {stack_trace}")


# Task 2: Read a CSV File
def read_employees():
    # Create empty dictionary
    my_dict = {}

    # Create list of rows
    rows = []

    # Read a csv file
    try:
        with open("../csv/employees.csv") as csvfile:
            reader = csv.reader(csvfile, delimiter=',')

            # Get only the first line
            my_dict["fields"] = next(reader)

            # Read each row and save to list of rows
            for row in reader:
                rows.append(row)
                
            my_dict["rows"] = rows
        return my_dict
                
    except Exception as e:
        print_stack_trace(e)


employees = read_employees()
print(employees)


# Task 3: Find the Column Index
def column_index(string):
    index = employees["fields"].index(string)
    return index


employee_id_column = column_index("employee_id")


# Task 4: Find the Employee First Name
def first_name(row_number):
    # Get index column for first names
    index = column_index("first_name")

    # Get the row with the employee information
    employee_row = employees["rows"][row_number]

    # Turn employee info row into a list and return the item at the index for the first names
    return list(employee_row)[index]


# Task 5: Find the Employee: a Function in a Function
def employee_find(employee_id):
    # employee_match gets the row where the employee id matches and returns as integer
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    
    # Use filter() to find all instances of the employee and return as a list
    matches = list(filter(employee_match, employees["rows"]))
    return matches


# Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
    # Use lambda to use the input row to access the row and column where the . Filter the iterable `employees["rows"]` where the row is the employee id
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
    return matches


employee_last_name_column = column_index("last_name")
print(employee_last_name_column)


# Task 7: Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    employees["rows"].sort(key=lambda row : row[employee_last_name_column])
    return employees["rows"]


sort_by_last_name()
print(employees)


# Task 8: Create a dict for an Employee
def employee_dict(employee_data):
    num = len(employees["fields"])
    return dict(zip(employees["fields"][1:num], employee_data[1:num]))


print(employee_dict(employees["rows"][0]))


# Task 9: A dict of dicts, for All Employees
def all_employees_dict():
    # Create empty lists for ids and employee dicts
    ids = []
    employee_dicts = []

    # Iterate through rows and append ids and dicts to lists
    for row in employees["rows"]:
        ids.append(row[0])
        employee_dicts.append(employee_dict(row))
    
    # Return the dict created from the list of ids and dicts
    return dict(zip(ids, employee_dicts))


print(all_employees_dict())


# Task 10: Use the os Module
def get_this_value():
    return os.environ.get("THISVALUE")


# Task 11: Creating Your Own Module
def set_that_secret(secret):
    custom_module.set_secret(secret)


set_that_secret("thissecret")
print(custom_module.secret)


# Helper function to create dict from file and convert rows to tuples
def create_dict(file):
    # Create empty dictionary
    my_dict = {}

    # Create list of rows
    rows = []

    # Read a csv file
    try:
        with open(file) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')

            # Get only the first line
            my_dict["fields"] = next(reader)

            # Read each row and save to list of rows
            for row in reader:
                tuple_row = tuple(row)
                rows.append(tuple_row)
                
            my_dict["rows"] = rows
        return my_dict
                
    except Exception as e:
        print_stack_trace(e)


# Task 12: Read minutes1.csv and minutes2.csv
def read_minutes():
    dict1 = create_dict('../csv/minutes1.csv')
    dict2 = create_dict('../csv/minutes2.csv')

    return dict1, dict2


minutes1, minutes2 = read_minutes()
print(f"minutes1: {minutes1}\nminutes2: {minutes2}")


# Task 13: Create minutes_set
def create_minutes_set():
    # Combines the minutes sets
    minutes_set = set(minutes1["rows"]).union(minutes2["rows"])
    return minutes_set


minutes_set = create_minutes_set()


# Task 14: Convert to datetime
def create_minutes_list():
    # Turn minutes set into a list
    minutes_list = list(minutes_set)  

    # Use map to iterate through and convert to datetimes
    my_map = map(lambda entry : (entry[0], datetime.strptime(entry[1], "%B %d, %Y")), minutes_list)

    # return as list
    return list(my_map)


minutes_list = create_minutes_list()
print(minutes_list)


# Task 15: Write Out Sorted List
def write_sorted_list():
    # Sort minutes list using the datetime
    minutes_list.sort(key=lambda row : row[1])

    # Use map to convert datetime objects back to strings
    my_map = map(lambda row : (row[0], datetime.strftime(row[1], "%B %d, %Y")), minutes_list)

    # Write minutes to csv file
    try:
        with open('./minutes.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(minutes1["fields"])
            writer.writerows(minutes_list)
            
    except Exception as e:
        print_stack_trace(e)

    return list(my_map)
