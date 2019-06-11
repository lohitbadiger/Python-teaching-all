class Employee:
    def __init__(self,name,address):
        self.name=name
        self.address=address


    def fullname(self):
        return '{} {}'.format(self.name,self.address)

emp1=Employee('rekha','hubli')
emp12 =Employee('loh', 'hubli')

print(Employee.fullname(emp12))

print(emp1.fullname())
print(emp12.fullname())