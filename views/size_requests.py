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
    return SIZES

def get_single_size(id):
    """returns a specified size dictionary by comparing the primary key of the dictionary to the id argument"""
    requested_size=None
    for size in SIZES:
        if size["id"]==id:
            requested_size=size
    return requested_size