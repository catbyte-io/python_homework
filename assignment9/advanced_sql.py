import sqlite3
from datetime import datetime

# Task 1: Complex JOINs with Aggregation
# Find the total price of each of the first 5 orders.
# Print out the order_id and the total price for each of the rows returned.

with sqlite3.connect("../db/lesson.db") as conn:

    conn.execute("PRAGMA foreign_keys = 1")

    cursor = conn.cursor()

    sql_statement = """
        SELECT o.order_id, SUM(p.price * li.quantity)
        FROM orders o
        JOIN line_items li ON o.order_id = li.order_id JOIN products p ON li.product_id = p.product_id
        GROUP BY o.order_id
        ORDER BY o.order_id LIMIT 5;
""" 

    try:
        cursor.execute(sql_statement)
        results = cursor.fetchall()
        print("Price of first five orders:")
        if len(results) > 0:
            for row in results:
                print(row)
        else:
            print("No orders yet.")

    except Exception as e:
        print(e)


    # Task 2: Understanding Subqueries
    # For each customer, find the average price of their orders.
    sql_statement_2 = """
        SELECT c.customer_name, AVG(total_price)
        FROM customers c
        LEFT JOIN (
            SELECT customer_id AS customer_id_b, SUM(p.price * li.quantity) AS total_price
            FROM orders o JOIN line_items li ON o.order_id = li.order_id
            JOIN products p ON li.product_id = p.product_id
            GROUP BY customer_id
        ) o ON customer_id = customer_id_b
        GROUP BY c.customer_id
"""

    try:
        cursor.execute(sql_statement_2)
        results = cursor.fetchall()
        print("Average price of customer orders:")
        if len(results) > 0:
            for row in results:
                print(row)
        else:
            print("No orders yet.")

    except Exception as e:
        print(e)

    # Task 3: An Insert Transaction Based on Data
    try:
        # Get the customer id
        cursor.execute("SELECT c.customer_id  FROM customers c  WHERE c.customer_name = 'Perez and Sons';")
        customer_id = cursor.fetchone()[0]

        # Get the employee id
        cursor.execute("SELECT e.employee_id FROM employees e WHERE e.first_name = 'Miranda' AND e.last_name = 'Harris';")
        employee_id = cursor.fetchone()[0]
    
        # Get product ids of the 5 least expensive items
        cursor.execute("SELECT p.product_id FROM products p ORDER BY p.price ASC LIMIT 5;")
        product_ids = [row[0] for row in cursor.fetchall()]
        if not product_ids:
            raise Exception("No products found.")
    
        date = datetime.now().strftime("%Y-%m-%d")

        # Create order
        cursor.execute("INSERT INTO orders (customer_id, employee_id, date) VALUES (?,?,?) RETURNING (order_id)", (customer_id, employee_id, date))
        order_id = cursor.fetchone()[0]

        # Prepare data by creating tuples
        items = []
        for prod_id in product_ids:
            item = (order_id, prod_id, 10)
            items.append(item)

        # Create line items for order
        cursor.executemany("INSERT INTO line_items (order_id, product_id, quantity) VALUES (?,?,?)", (items))
        
        # Commit the transaction
        conn.commit()

    except (sqlite3.IntegrityError, Exception) as e:
        print("The following error occurred:", e)
        conn.rollback()  # Rollback the transaction if an error occurs
    
    # Get the line_item_id, quantity, and product name from the order
    cursor.execute("SELECT li.line_item_id, li.quantity, p.product_name FROM line_items li JOIN orders o ON o.order_id = li.order_id JOIN products p ON p.product_id = li.product_id WHERE o.order_id = ?", (order_id,))
    results = cursor.fetchall()
    if results:
        print("Task 3 Results:")
        for row in results:
            print(row)
    else:
        raise Exception(f"No line items found for order {order_id}.")

    
    # Task 4: Aggregation with HAVING
    # Find all employees associated with more than 5 orders.  You want the first_name, the last_name, and the count of orders. 
    sql_statement_3 = """
        SELECT e.first_name, e.last_name, COUNT(o.order_id) AS num_orders
        FROM employees e JOIN orders o ON e.employee_id = o.employee_id
        GROUP BY e.employee_id
        HAVING num_orders > 5;
"""
    cursor.execute(sql_statement_3)
    results = cursor.fetchall()
    if results:
        print("Employees associated with more than 5 orders:")
        for row in results:
            print(row)
    else:
        print("No employees associated with more than 5 orders.")
