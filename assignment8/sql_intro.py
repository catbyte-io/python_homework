import sqlite3
from datetime import datetime


# Task 1: Create a New SQLite Database
with sqlite3.connect("../db/magazines.db") as conn:

    conn.execute("PRAGMA foreign_keys = 1")

    # Task 2: Define Database Structure
    cursor = conn.cursor()

    try:
        # Create tables
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Publishers (
            publisher_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Magazines (
            magazine_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            publisher_id INTEGER,
            FOREIGN KEY (publisher_id) REFERENCES Publishers (publisher_id)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Subscribers (
            subscriber_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            address TEXT NOT NULL
        )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Subscriptions (
            subscription_id INTEGER PRIMARY KEY,
            magazine_id INTEGER,
            subscriber_id INTEGER,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (magazine_id) REFERENCES Magazines (magazine_id)
        )
        """)

        conn.commit()

    except sqlite3.IntegrityError:
        print("An error occurred.")


# Helper function to get an expiration date that is one year from the current day and convert to string
def set_expiration():
    today = datetime.now()
    one_year = today.replace(year=today.year + 1)
    exp_date = one_year.strftime("%Y-%m-%d")
    return exp_date

# Task 3: Populate Tables with Data
def add_publisher(cursor, name):
    try:
        cursor.execute("INSERT INTO Publishers (name) VALUES (?)", (name,))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")


def add_magazine(cursor, name, publisher):
    try:
        cursor.execute("SELECT * FROM Publishers WHERE name = ?", (publisher,))
        results = cursor.fetchall()
        if len(results) > 0:
            publisher_id = results[0][0]
        else:
            print(f"Publisher {publisher} for magazine not found")
            return
        cursor.execute("INSERT INTO Magazines (name, publisher_id) VALUES (?,?)", (name, publisher_id))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")


def add_subscriber(cursor, name, address):
    try:
        cursor.execute("INSERT INTO Subscribers (name, address) VALUES (?,?)", (name, address))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")


def create_subscription(cursor, subscriber, address, magazine):
    try:
        # Try to find subscriber
        cursor.execute("SELECT * FROM Subscribers WHERE name = ? AND address = ?", (subscriber, address))
        results = cursor.fetchall()
        if len(results) > 0:
            subscriber_id = results[0][0]
        else:
            print(f"Subscriber {subscriber} not found.")
            return
        
        # Select magazine
        cursor.execute("SELECT * FROM Magazines WHERE name = ?", (magazine,))
        results = cursor.fetchall()
        if len(results) > 0:
            magazine_id = results[0][0]
        else:
            print(f"Magazine titled {magazine} not found.")
            return

        # Set the expiration date for one year from now
        expiration_date = set_expiration()
        
        # Add the subscription
        cursor.execute("INSERT INTO Subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?,?,?)", (subscriber_id, magazine_id, expiration_date))

    except sqlite3.IntegrityError:
        print(f"Subscription already exists.")


with sqlite3.connect("../db/magazines.db") as conn:

    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    # Add publishers
    publishers = ["Red Line", "Yong Com", "Currents"]

    for publisher in publishers:
        add_publisher(cursor, publisher)

    magazines = [("Electric Beat", "Red Line"), ("Wind Breaker", "Yong Com"), ("CyberGuardian", "Currents")]
    
    for magazine_name, publisher_name in magazines:
        add_magazine(cursor, magazine_name, publisher_name)
    
    subscribers = [("Jody Yuhas", "1425 Sycamore, Salmon ID", "Electric Beat"), ("Klint Hondel", "829 Five Mile Creek, Taos NM", "CyberGuardian"), ("Georgia Harris", "1355 Tamarack Drive, Tuscon AZ", "Wind Breaker")]

    for sub_name, sub_address, magazine_name in subscribers:
        add_subscriber(cursor, sub_name, sub_address)
        create_subscription(cursor, sub_name, sub_address, magazine_name)


    # Task 4: Write SQL Queries
    # Write a query to retrieve all information from the subscribers table.
    cursor.execute("SELECT * FROM Subscribers")
    subscriber_info = cursor.fetchall()
    if len(subscriber_info) > 0:
        print("Subscriber info:")
        for row in subscriber_info:
            print(row)
    else:
        print("No subscribers yet.")

    # Write a query to retrieve all magazines sorted by name.
    cursor.execute("SELECT * FROM Magazines ORDER BY name")
    magazine_info = cursor.fetchall()
    if len(magazine_info) > 0:
        print("Magazine info:")
        for row in magazine_info:
            print(row)

    # Write a query to find magazines for a particular publisher, one of the publishers you created. This requires a JOIN.
    cursor.execute("SELECT m.name FROM Magazines AS m JOIN Publishers AS p ON m.publisher_id = p.publisher_id WHERE p.name = ?", (publishers[1],))
    pub_magazines = cursor.fetchall()
    if len(pub_magazines) > 0:
        print("Magazines published by Yong Com:")
        for row in pub_magazines:
            print(row)
    else:
        print("No magazines found for thsi publisher.")
    # Add these queries to your script. For each, print out all the rows returned by the query.
