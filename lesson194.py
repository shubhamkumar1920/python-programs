# class methods
# difference between class methods and instance methods

class Person:
    count_instance = 0
    def __init__(self,first_name,last_name,age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def count_instances(cls):
        return f"you have created {cls.count_instance} of {cls.__name__} class"
    

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def is_above_18(self):
        return self.age>18

p1 = Person('Harshit','Vashistha',10)
p2 = Person('Shubham','Kumar',24)
"you have created 4 instances of person class"

print(Person.count_instances())
