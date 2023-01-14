import time

ORDERS=[]

def get_all_orders():
    """returns the ORDERS list of dictionaries"""
    return ORDERS

def get_single_order(id):
    """returns a single order dictionary by comparing the primary key to the id argument"""
    requested_order=None
    for order in ORDERS:
        if order["id"]==id:
            requested_order=order
    return requested_order

def create_order(order):
    """Posts order dictionary to ORDERS list, 
    add incrementing id and time, based on Date.now()"""
    max_id=0

    if len(ORDERS)>0:
        max_id = ORDERS[-1]["id"]
    
    new_id = max_id + 1
    seconds = time.time()
    order["id"] = new_id
    milliseconds = seconds * 1000
    order["date"] = round(milliseconds)
    ORDERS.append(order)

    return order

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