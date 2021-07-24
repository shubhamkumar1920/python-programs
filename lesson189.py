class Laptop:
    discount_percent = 10
    def __init__(self,brand,model_name,price):
        # instance variables
        self.brand = brand
        self.name = model_name
        self.price = price
        self.laptop_name = brand + ' ' + model_name

    def apply_discount(self):
        # self.price
        off_price = (Laptop.discount_percent/100)*self.price
        return self.price - off_price

laptop1 = Laptop('hp','au114tx',63000)
laptop2 = Laptop('apple','macbook pro',230000)
print(laptop1.apply_discount())