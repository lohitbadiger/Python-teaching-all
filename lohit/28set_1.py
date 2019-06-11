def person(dictionary):
    belts =list(dictionary.values())
    for belt in belts:
        num = belts.count(belt)
        print(f'there are {num} {belt} belts ')


lohit_items = {}

while True:
    lohit_program = input('enter name of belt :')
    lohit_frame = input('enter the name of belt color: ')
    lohit_items[lohit_program] = [lohit_frame]

    another = input('add another program? (y/n)')
    if another == 'y': 
        continue
    else:
        break

person(lohit_items)
