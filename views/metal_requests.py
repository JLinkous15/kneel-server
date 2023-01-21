import sqlite3
import json
from models import Metal

METALS=[
    {
        "id":1,
        "name":"gold",
        "price":40
    },
    {
        "id":2,
        "name":"silver",
        "price":30
    },
    {
        "id":3,
        "name":"palladium",
        "price":100
    },
    {
        "id":4,
        "name":"sterling",
        "price":27
    },
    {
        "id":5,
        "name":"zirconium",
        "price":35
    }
]

def get_all_metals():
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT *
        FROM metals
        """)

        metals = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            metal = Metal(row["id"], row["metal"], row["price"])
            metals.append(metal.__dict__)
        return metals

def get_single_metal(id):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT *
        FROM metals m
        where m.id = ?
        """, (id,))

        data = db_cursor.fetchone()
        response = Metal(data["id"], data["metal"], data["price"])

        return response.__dict__