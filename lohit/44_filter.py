# easy way to handle functions


grades=['A','B','A','C','F','C',"D"]

def remove_F(grade):
    return grade!='F'


print(list(filter(remove_F, grades)))

# using for loop

filtered_grade=[]
for grade in grades:
    if grade!='A':
        filtered_grade.append(grade)
print(filtered_grade)

# # # using Comprehesion

filtered_grade = [grade for grade in grades  if grade != 'B']
print(filtered_grade)