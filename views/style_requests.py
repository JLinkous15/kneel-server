import json
import sqlite3
from models import Style

STYLES=[
    {
        "id":1,
        "name":"ring",
        "price":20
    },
    {
        "id":2,
        "name":"bracelet",
        "price":50
    },
    {
        "id":3,
        "name":"earring",
        "price":15
    },
    {
        "id":4,
        "name":"necklace",
        "price":65
    },
    {
        "id":5,
        "name":"toe ring",
        "price":25
    },
]

def get_all_styles():
    """returns the STYLES list of dictionaries"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT *
        FROM styles
        """)
        styles = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            style = Style(row["id"], row["name"], row["price"])
            styles.append(style.__dict__)
        return styles

def get_single_style(id):
    """returns a single style dictionary by comparing the id argument to the primary key"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT *
        FROM styles s
        WHERE s.id = ?
        """,(id,))
        data = db_cursor.fetchone()
        style = Style(data["id"], data["name"], data["price"])
        return style.__dict__