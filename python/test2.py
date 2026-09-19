class shop:
    item_count = 0
    @classmethod
    def get_count(cls):
        print(f"The no of item are {shop.item_count}")
    def __init__(self, name, price):
        self.name = name
        self.price = price
        shop.item_count += 1

    def get_info(self):
        print(f"The item is {self.name} and its price is {self.price}")

    @staticmethod
    def discount(price ,percentage):
        print(f"Discounted price is {price - (price * percentage / 100)}")

item1 = shop("apple", 1)
item2 = shop("banana", 2)
item2.get_info()
item3 = shop("mango", 5)
shop.get_count()
shop.discount(5, 10)
