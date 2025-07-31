# Task 3: List Comprehension Practice
import csv
import traceback


# List to contain all employees lists
all_employees = []

try:
    with open('../csv/employees.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            all_employees.append(row)

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


# Create list of employees
employee_list = [x for x in all_employees]
print(employee_list)

# Create list of employee names
employee_names = [x[1] + " " + x[2] for x in employee_list[1:]] 
print(employee_names)

# Create list of names with e
e_names = [x for x in employee_names if "e" in x]
print(e_names)
