# 1. Inventory Management System (IMS)
# 📌 Question:
# Develop a simple inventory management system for a small retail shop: Write a program to demonstrate how objects representing different inventory items are created and how basic methods can be used to display or manipulate their properties.

# 📖 Explanation:
# Items are objects with properties (name, price, quantity). Methods display and update data.

class Item:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

    def display(self):
        print("Item:", self.name)
        print("Price:", self.price)
        print("Quantity:", self.qty)

    def update_qty(self, q):
        self.qty += q

i = Item("Pen", 10, 5)
i.update_qty(2)
i.display()