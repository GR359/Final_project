import sqlite3
import json
from fastapi import FastAPI

connection = sqlite3.connect("db.sqlite")
cursor = connection.cursor()

        
# Create tables
cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY,
                name TEXT,
                phone TEXT
            )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY,
                name TEXT,
                price REAL
            )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY,
                timestamp INTEGER,
                customer_id INTEGER,
                notes TEXT,
                FOREIGN KEY (customer_id) REFERENCES customers(id)
            )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS order_items (
                order_id INTEGER,
                item_id INTEGER,
                FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE ON UPDATE CASCADE,
                FOREIGN KEY (item_id) REFERENCES items(id) ON DELETE CASCADE ON UPDATE CASCADE
            )''')

with open("customers.json") as f:
    customers = json.load(f)
    for phone, name in customers.items():
        cursor.execute("INSERT INTO customers (name, phone) VALUES (?, ?);", (name,phone))
with open("items.json") as f:
    items = json.load(f)
    for name, stats in items.items():
        price = stats["price"]
        number_of_orders = stats["orders"]
        cursor.execute("INSERT INTO items (name, price) VALUES (?, ?);", (name,price))