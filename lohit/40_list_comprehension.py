# list conprehensions

# normal way
numbers=[1,2,34,4,6]

double=[]

for number in numbers:
    double.append(number*2)
print(double)

# =============================
double.append(number*2 for number in numbers)
print('this is the comprehension way::',double)