# multilevel inheritence,MRO,method overridding
# more_about_inheritence
# can we derive more than one class from base class?
# multilevel inheritence
# method resolution order
# method overridding
# isinstance(),issubclass()

class Phone:  #base class / parent class
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self.price = price

    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def make_a_call(self,number):
        return f"callin {number}...."



class Smartphone(Phone): #derived/child class
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):
        # self.brand = brand
        # self.model_name = model_name
        # self.price = price
        #two ways
        Phone.__init__(self,brand,model_name,price)
        super().__init__(brand,model_name,price)

        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

    def full_name(self):
        return f"{self.brand} {self.model_name} and price is {self.price}"

    def make_a_call(self,number):
        return f"callin {number}...."

class FlagshipPhone(Smartphone):
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera,front_camera):
        super().__init__(brand,model_name,price,ram,internal_memory,rear_camera)
        self.front_camera = front_camera

    def full_name(self):
        return f"{self.brand} {self.model_name} and price is {self.price} and front_camera = {self.front_camera}"





phone = Phone('nokia','1100',1000)
smartphone = Smartphone('oneplus','5','30000','6 GB','64 GB','20MP')
print(phone.full_name())
print(smartphone.full_name() +"and price is {}")
oneplus5t = FlagshipPhone('oneplus','5','30000','6 GB','64 GB','20MP','16 MP')
# print(help(Smartphone))

print(isinstance(oneplus5t, Smartphone))
print(isinstance(Smartphone,FlagshipPhone))