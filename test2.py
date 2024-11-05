import csv
class product:
    def __init__(self,name:str,price: float, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity
    @classmethod
    def list_items(cls):
        with open('items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
            for item in items:
                print(item)
    def Total_price(self):
        return self.price * self.quantity
    def __str__(self):
        return f"{self.name}: cost {self.price}, quantity:{self.quantity}"
class store:
    def __init__(self,product,quantity):
        self.products = []
        self.product = product
        self.quantity = quantity
    @classmethod
    def store_csv(cls):
        with open('store.csv','r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                store = row("store")
                product = row("product")
                quantity = row("quantity")
    def add_product(self,product):
        return self.products.append(product)
    def remove_product(self,product):
        return self.products.remove(product)
    def total_store_price(self):
        return sum(product.Total_price() for product in self.products)
product.list_items()