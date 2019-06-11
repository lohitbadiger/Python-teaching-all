# _increament_salery.
class emplpyee:
    
    increase=2
    def __init__(self,pay,name,age):
        self.pay=pay
        self.name=name
        self.age=age

    
    def fullname(self):
        return '{} {}'.format(self.name,self.age)
    

    def salery_hike(self):
        self.pay = int(self.pay * emplpyee.increase)
        # i can use the class name i,e 'emplyee' 
    #    elf.pay = int(self.pay * emplpyee.increase)


lohit=emplpyee(2,'lohit',21)
rekha=emplpyee(3,'rekha',23)


print(lohit.pay)
lohit.salery_hike()
print(lohit.pay)
print(lohit.__dict__)

lohit.increase=10

# to print the value instence holding
print(lohit.__dict__)

print(lohit.increase)
print(lohit.name)