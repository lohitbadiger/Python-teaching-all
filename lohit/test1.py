class Tab:
    menu={
    'wine':5,
    'soft_drink':3,
    'beer':2,
    'chicken':20,
    'beef':29

    }

    def __init__(self):
        self.total=0
        self.items=[]

    def add(self,item):
        self.items.append(item)
        self.total+=self.menu[item]
        

    def print_bill(self,tax,service):
        tax=(tax/100)*self.total
        service=(service/100)*self.total
        total=self.total+tax+service


        for item in self.items:
            print(f'{item:2} ${self.menu[item]}')

        print(f'{"Total":2} ${total:.2f}')