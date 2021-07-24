# create a laptop class with attributes like brand name,model name,price
# create two objects/instance of your laptop class

class Laptop:
    def __init__(self,brand,name,price):
        # instance variables
        self.brand = brand
        self.name = name
        self.price = price
        #self.laptop_name = brand + '  ' + model_name

laptop1 = Laptop('hp','au114tx','63000')
print(laptop1.name)