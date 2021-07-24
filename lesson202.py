# special magic method/dunder methods
# operator overloading
# polymorphism

class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def phone_name(self):
        return f"{self.brand} {self.model}"

    # str, repr
    def __str__(self):
        return f'{self.brand} {self.model} and price is {self.price}'

    def __repr__(self):
        return f'Phone(\'{self.brand}\',\' {self.model}\',{self.price}'

    def __len__(self):
        return len(self.phone_name())

    # def __mul__(self,other):
    #     return self.price * other.price


# l = [1,2,3]
# print(l)
my_phone = Phone('nokia','1100',1000)
print(str(my_phone))
print(repr(my_phone))
print(my_phone.__repr__())

class Smartphone(Phone): #derived/child class
    def __init__(self, brand, model, price, camera):
        super().__init__(brand, model, price)
        self.camera = camera

    def phone_name(self):
        return f"{self.brand} {self.model} and price is {self.price}"

    def __len__(self):
        return self.price

my_phone = Phone('nokia', '1100' , 1000)
my_phone2 = Phone('nokia', '1600', 1200)
my_smartphone = Smartphone('oneplus','5t',33000,'16 MP')
print(my_smartphone.phone_name())
print(my_phone.phone_name())
print(len(my_smartphone))
print(len(my_phone))