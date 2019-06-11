def belt_count(dictionary):
    belts = list(dictionary.values())
    for belt in belts:
        num = belts.count(belt)
        print(f'there are {num} {belt} belts ')


lohit_belts = {}

while True:
    lohit_program = input('enter name of belt :')
    lohit_frame = input('enter the name of belt color: ')
    lohit_belts[lohit_program] = [lohit_frame]

    another = input('add another program? (y/n)')
    if another == 'y': 
        continue
    else:
        break
belt_count(lohit_belts)
