class Menu:
    """fill in class definition here"""
    def __init__(self):
        self.orders = dict()
    
    def add(self, item, qty):
        self.orders[item] = qty
        
    def show(self):
        for k, v in self.orders.items():
            print(k, v)

m = Menu()  # Menu is a class
m.add("idly", 10)
m.add("vada", 20)

m.show()