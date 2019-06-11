class planet:

    def __init__(self):
        self.name = 'lohit'
        self.game = 'Counter Strike'
        self.number = 3243
        self.rate = 5
    
    def orbit(self):
        return f'{self.name} is {self.number}'
    

lohit = planet()
print(f'Name is : {lohit.name}')
print(f'Game is : {lohit.game}')
print(f'Number Is : {lohit.number}')

print(lohit.orbit()) 