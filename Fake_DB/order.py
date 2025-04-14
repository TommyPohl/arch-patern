class Order:
    def __init__(self, items):
        self.items = items

    def get_price(self):
        result = 0
        for item in self.items:
            result += item.price

        return result

    #def __str__(self):
    #    pass