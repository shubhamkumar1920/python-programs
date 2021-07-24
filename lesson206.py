# raise error example 2
class Mobile:
    def __init__(self,name):
        self.name = name

class MobileStore:
    def __init__(self):
        self.mobiles = []

    def add_mobile(self,new_mobile):
        if isinstance(new_mobile, Mobile):
            self.mobiles.append(new_mobile)

        else:
            raise TypeError('NEW MOBILE SHOULD BE OBJECT OF MOBILE CLASS')

oneplus = Mobile('one plus 6')
samsung = 'samsung galaxy s8'
mobostore = MobileStore()
print(mobostore.mobiles)
# mobostore.add_mobile(samsung)
print(mobostore.mobiles)
mobo_phones = mobostore.mobiles
print(mobo_phones[0])
