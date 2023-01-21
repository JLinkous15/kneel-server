class Order():
    def __init__(self, id, metal_id, size_id, style_id, total):
        self.id = id
        self.metal_id = metal_id
        self.size_id = size_id
        self.style_id = style_id
        self.total = round(total, 3)

