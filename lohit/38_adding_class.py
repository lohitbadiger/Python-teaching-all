# this program is to increase the number of empployees each time the new emp is add
class emplpyee:
    
    add_emp=0
    increase=2
    def __init__(self,pay,name,age):
        self.pay=pay
        self.name=name
        self.age=age

        emplpyee.add_emp+=1
    def fullname(self):
        return '{} {}'.format(self.name,self.age)
    

    def salery_hike(self):
        self.pay = int(self.pay * self.increase)
    

# countes the number of employess


print(emplpyee.add_emp)

lohit=emplpyee(2,'lohit',21)
print(emplpyee.add_emp)

rekha=emplpyee(3,'rekha',23)
print(emplpyee.add_emp)

lohi=emplpyee(3,2,43)

#countes the number of employess

print(emplpyee.add_emp)
