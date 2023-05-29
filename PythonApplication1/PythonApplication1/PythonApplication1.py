# -*- coding: cp1252 -*-

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    def update_quantity(self, quantity):
        self.quantity += quantity

    def __str__(self):
        return f"Produkt: {self.name}, Cena: {self.price} zl, Ilosc: {self.quantity}"


class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product, quantity):
        for p in self.products:
            if p.get_name() == product.get_name():
                p.update_quantity(quantity)
                return
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def calculate_total_price(self):
        total_price = 0
        for product in self.products:
            total_price += product.get_price() * product.get_quantity()
        return total_price


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.shopping_cart = ShoppingCart()

    def add_to_cart(self, product, quantity):
        self.shopping_cart.add_product(product, quantity)

    def remove_from_cart(self, product):
        self.shopping_cart.remove_product(product)

    def checkout(self):
        total_price = self.shopping_cart.calculate_total_price()
        print("Dziekujemy za zakupy, {}!".format(self.name))
        print("Laczna suma: {} zl".format(total_price))
        self.shopping_cart = ShoppingCart()


product1 = Product("Laptop", 999, 2)
product2 = Product("Myszka", 20, 5)
product3 = Product("Klawiatura", 50, 3)

customer = Customer("Michal", "michal@example.com")

customer.add_to_cart(product1, 1)
customer.add_to_cart(product2, 2)
customer.add_to_cart(product3, 1)

total_price = customer.shopping_cart.calculate_total_price()
print("Laczna kwota w koszyku: {} zl".format(total_price))

customer.remove_from_cart(product2)

total_price = customer.shopping_cart.calculate_total_price()
print("Laczna kwota w koszyku po usunieciu produktow: {} zl".format(total_price))

customer.checkout()
