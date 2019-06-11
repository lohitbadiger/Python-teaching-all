# _increament_salery.
class emplpyee:
    def __init__(self,pay,name,age):
        self.pay=pay
        self.name=name
        self.age=age

    
    def fullname(self):
        return '{} {}'.format(self.name,self.age)
    

    def salery_hike(self):
        self.pay=int(self.pay*2.0)


lohit=emplpyee(2,'lohit',21)
rekha=emplpyee(3,'rekha',23)

print(lohit.pay)    
lohit.salery_hike()
print(lohit.pay)
