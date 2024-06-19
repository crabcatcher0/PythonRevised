class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
        return "Quantity is updated."

    def __str__(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"
    
class Inventory:
    def __init__(self):
        self.products = []

    def add_products(self, product):
        self.products.append(product)
        return f"Product added."

    def update_product(self, product_id, new_quantity):
        for product in self.products:
            if product.product_id == product_id:
                product.update_quantity(new_quantity)
                break
    
    def display_inventory(self):
        for product in self.products:
            print(product)
        if not self.products:
            print("Inventory is empty.")


product1 = Product(1, "Shoe", 1120, 4)
print(product1.update_quantity(5))
info = Inventory()
print(info.update_product(1, 45))