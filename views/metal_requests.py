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
    """returns entire list of metal dictionaries"""
    return METALS

def get_single_metal(id):
    """returns single metal with and id matching the parsed url"""
    requested_metal=None

    for metal in METALS:
        if metal["id"]==id:
            requested_metal=metal

    return requested_metal