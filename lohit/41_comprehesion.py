# squaring  the only even number in list.

numbers=[1,2,3,4,5,6,7,8,9]

square=[]

for number in numbers:
    if (number ** 2) % 2 == 0:
        square.append(number**2)
print(square)

# ====This is normal way============

#now compreshion way

square = [number ** 2 for number in numbers if (number ** 2) % 2 == 0 ]
print("_",square)