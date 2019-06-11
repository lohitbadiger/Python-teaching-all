number=[1,2,3,4,5,6,7,8,9,10]

add=[]

for num in number:
    if (num%2)==0:
        add.append(num+1)
print(add)


# comprehesion way

add=[num + 1 for num in number  if (num % 2) == 0]
print(add)