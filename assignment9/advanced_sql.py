import sqlite3

# Task 1: Complex JOINs with Aggregation
# Find the total price of each of the first 5 orders.
# Print out the order_id and the total price for each of the rows returned.

with sqlite3.connect("../db/lesson.db") as conn:

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
