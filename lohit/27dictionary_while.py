def lohit(dictionary):
    for key,val in dictionary.items():
        print(f'Im a {key} and this is {val}')

lohit_pgram= {}

while True:
    lohit_name= input('enter name of programming')
    lohit_frame=input('enter the name of frame work')
    lohit_pgram[lohit_name]=[lohit_frame]

    another=input('add another program? (y/n)')
    if another=='y':
        continue
    else:
        break

lohit(lohit_pgram)