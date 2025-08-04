# Task 1: Introduction to Pandas - Creating and Manipulating DataFrames
import pandas as pd


# Task 1: Introduction to Pandas - Creating and Manipulating DataFrames
# Create dictionary
my_dict = {"Name": ["Alice", "Bob", "Charlie"],
           "Age": [25, 30, 35],
           "City": ["New York", "Los Angeles", "Chicago"]}

# Convert dictionary to DataFrame
task1_data_frame = pd.DataFrame(my_dict)
print(task1_data_frame)

# Make a copy of the DataFrame
task1_with_salary = task1_data_frame.copy()

# Add a column to the DataFrame
task1_with_salary["Salary"] = [70000, 80000, 90000]
print(task1_with_salary)

# Modify existing column
task1_older = task1_with_salary.copy()
task1_older["Age"] += 1
print(task1_older)
