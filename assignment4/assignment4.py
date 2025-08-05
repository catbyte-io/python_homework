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

# Save the DataFrame as a CSV file
task1_older.to_csv("employees.csv", index=False)


# Task 2: Loading Data from CSV and JSON
# Read data from a CSV file
task2_employees = pd.read_csv("employees.csv")
print(task2_employees)

# Read data from JSON file
json_employees = pd.read_json("additional_employees.json")
print(json_employees)

# Combine DataFrames
frames = [task2_employees, json_employees]
more_employees = pd.concat(frames, ignore_index=True)
print(more_employees)


# Task 3: Data Inspection - Using Head, Tail, and Info Methods
# Use the head() method
first_three = more_employees.head(n=3)
print(first_three)

# Use the tail() method
last_two = more_employees.tail(n=2)
print(last_two)

# Get the shape of the DataFrame
employee_shape = more_employees.shape
print(employee_shape)

# Use the info() method
print(more_employees.info())


# Task 4: Data Cleaning
dirty_data = pd.read_csv("dirty_data.csv")
print(f"Dirty Data:\n{dirty_data}")

clean_data = dirty_data.copy()

# Remove duplicate rows
clean_data = clean_data.drop_duplicates(ignore_index=True)
print(f"Removed Duplicate Rows:\n{clean_data}")

# Covert age to numeric and handle missing values
clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors="coerce")
print(f"Converted Age to Numeric:\n{clean_data}")

# Convert Salary to numeric, replacing known placeholders with NaN
clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors="coerce")
print(f"Converted Salary to Numeric:\n{clean_data}")

# Fill missing numeric values (use fillna). Fill Age whith the mean and Salary with the median
clean_data["Age"] = clean_data["Age"].fillna(value=clean_data["Age"].mean())
clean_data["Salary"] = clean_data["Salary"].fillna(value=clean_data["Salary"].median())
print(f"Filled Missing Numeric:\n{clean_data}")


