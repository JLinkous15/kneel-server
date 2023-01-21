import time
import json
import sqlite3
from models import Order

ORDERS=[]

def get_all_orders():
    """returns the ORDERS list of dictionaries"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT 
            o.id,
            o.metal_id,
            o.size_id,
            o.style_id,
            m.price + sz.price + s.price AS total_price
        FROM orders o
        JOIN metals m ON m.id = o.metal_id
        JOIN sizes sz ON sz.id = o.size_id
        JOIN styles s ON s.id = o.style_id
        """)
        orders = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            order = Order(row["id"], row["metal_id"], row["size_id"], row["style_id"], row["total_price"])
            orders.append(order.__dict__)
        return orders

def get_single_order(id):
    """returns a single order dictionary by comparing the primary key to the id argument"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT 
            o.id,
            o.metal_id,
            o.size_id,
            o.style_id,
            m.price + sz.price + s.price AS total_price
        FROM orders o
        JOIN metals m ON m.id = o.metal_id
        JOIN sizes sz ON sz.id = o.size_id
        JOIN styles s ON s.id = o.style_id
        WHERE o.id = ?
        """, (id,))
        data = db_cursor.fetchone()
        order = Order(data["id"], data["metal_id"], data["size_id"], data["style_id"], data["total_price"])
        return order.__dict__

def create_order(new_order):
    """Posts order dictionary to ORDERS list, 
    add incrementing id and time, based on Date.now()"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
    INSERT INTO orders
    VALUES (?, ?, ?, ?, ?)
    """, (None, new_order["metal_id"], new_order["size_id"], new_order["style_id"], None))

    id = db_cursor.lastrowid
    
    return get_single_order(id)

def delete_order(id):
    order_index=-1

    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            order_index=index
    if order_index >= 0:
        ORDERS.pop(order_index)

def update_order(id, new_order):
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            ORDERS[index] = new_order
            break