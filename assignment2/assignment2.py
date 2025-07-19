import csv
import traceback


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
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
            print(f"Exception type: {type(e)._name_}")
            message = str(e)
            if message:
                print(f"Exception message: {message}")
            print(f"Stack trace: {stack_trace}")

employees = read_employees()
print(employees)

# Task 3: Find the Column Index
def column_index(string):
    index = employees["fields"].index(string)
    return index

employee_id_column = column_index("employee_id")
print(employee_id_column)


# Task 4: Find the Employee First Name
def first_name(row_number):
    # Get index column for first names
    index = column_index("first_name")

    # Get the row with the employee information
    employee_row = employees["rows"][row_number]

    # Turn employee info row into a list and return the item at the index for the first names
    return list(employee_row)[index]

employee_first_name = first_name(9)
print(employee_first_name)

# Task 5: Find the Employee: a Function in a Function
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id


# Task 6: Find the Employee with a Lambda
# Task 7: Sort the Rows by las_name Using a Lambda
# Task 8: Create a dict for an Employee
# Task 9: A dict of dicts, for All Employees
# Task 10: Use the os Module
# Task 11: Creating Your Own Module
# Task 12: Read minutes1.csv and minutes2.csv
# Task 13: Create minutes_set
# Task 14: Convert to datetime
# Task 15: Write Out Sorted List
