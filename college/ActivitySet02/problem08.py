class Menu:
    """fill in class definition here"""
    def __init__(self):
        self.orders = dict()

    def __setitem__(self, k, v):
        self.orders[k] = v
        
    def __str__(self):
        return "\n".join(" ".join((k, str(v))) for k, v in self.orders.items())
    
m = Menu()
m["idly"] = 10
m["vada"] = 20

print(m)