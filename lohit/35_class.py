class Employee:

    def __init__(self, name, address):
        self.name = name
        self.address = address


emp1 = Employee('new person from', 'hubli')
emp12 = Employee('This is very bad', 'City')

print(emp1)
print(emp12)

print(emp1.name)
print(emp12.name)

print(emp1.address)