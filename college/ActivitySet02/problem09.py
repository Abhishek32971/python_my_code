

class Menu(dict):
    """fill in class definition here"""

    def __str__(self):
        return "\n".join(" ".join((k, str(v))) for k, v in self.items())


class Order:
    """fill in class definition here"""

    def __init__(self, menu):
        self.menu = menu
        self.orders = dict()

    def __setitem__(self, item, qty):
        self.menu[item] # Throws a key error if the ordered item is not in menu
        self.orders[item] = qty


class Bill:
    """fill in class definition here"""

    def __init__(self, menu, order):
        self.bill = sum(v * menu[k] for k, v in order.orders.items())

    def __str__(self):
        return f"Your total bill is: {self.bill} rupees"


m = Menu()
m["idly"] = 20
m["vada"] = 20

print(m)

o = Order(m)
try:
    o["vada"] = 2
    o["pongal"] = 2

except KeyError as e:
    print(e)

b = Bill(m, o)
print(b)