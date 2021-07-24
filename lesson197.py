# encapsulation
# abstraction
# some special naming convention
# name mangling
# _name -ye convention hai ye mean python me ye private hai 

class Phone:
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self.__price = price

    def make_a_call(self,phone_number):
        print(f"calling{phone_number}......")

    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def send_message(self):
        pass  #twilio

# _name # convention of private name
# __name__ # dunder/magic methods

Phone1 = Phone('nokia','1100',1000)
# print(Phone1.__price)
print(Phone1._Phone__price)
Phone1._phone__price = -1000
print(Phone1._Phone__price)
# print(Phone1.__dict__)


Phone1._price = -1000
print(Phone1._price)

l = [3,4,1,2]
l.sort()  #tim sort
print(l)