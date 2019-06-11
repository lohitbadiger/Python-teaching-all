def area(radius):
    return 3.142 * radius * radius
    

def volume(area,length):
        print(area * length)


radius=int(input('enter the value for the radius'))
length=int(input('enter the vlaue'))


volume(area(radius), length)