#how to use init function

class planet:
    
    def __init__(self, name, age, game, system):
        self.name=name
        self.age=age
        self.game=game
        self.system=system


    def orbit(self):
        return f'{self.name} is-------> {self.system}'

lohit=planet('lohit', 23, 'counter strike', 'windows')

print(f'Name is : {lohit.name}')
print(f'Name is : {lohit.age}')
print(f'Name is : {lohit.game}')
print(lohit.orbit())

naboo=planet('fgfd',6666,'game of thrones', 'Mac Os')

print(f'Name is: {naboo.name}')
print(f'Name is: {naboo.age}')
print(f'Name is: {naboo.game}')
print(naboo.orbit())


takuma=planet('takuma',32,23,'Android')

print(f'name is {takuma.name}')
print(f'name is {takuma.age}')
print(f'name is {takuma.game}')
print(takuma.orbit())


endo=planet("endo", 21,23,'Php')

print(f'name is {endo.name}')
print(f'name is {endo.age}')
print(f'name is {endo.game}')
print(endo.orbit())
