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
    return STYLES

def get_single_style(id):
    """returns a single style dictionary by comparing the id argument to the primary key"""
    requested_style=None
    for style in STYLES:
        if style["id"]==id:
            requested_style=style
    return requested_style