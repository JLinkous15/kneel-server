import json
import sqlite3
from models import Size

SIZES=[
    {
        "id":1,
        "size":"small",
        "price":0
    },
    {
        "id":1,
        "size":"medium",
        "price":1
    },
    {
        "id":1,
        "size":"large",
        "price":2
    },
]

def get_all_sizes():
    """returns the SIZES list of dictionaries"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT *
        FROM sizes
        """)
        sizes = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            size = Size(row["id"], row["size"], row["price"])
            sizes.append(size.__dict__)
        return sizes

def get_single_size(id):
    """returns a specified size dictionary by comparing the primary key of the dictionary to the id argument"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT *
        FROM sizes s
        WHERE s.id = ?
        """, (id,))
        data = db_cursor.fetchone()
        size = Size(data["id"], data["size"], data["price"])

        return size.__dict__