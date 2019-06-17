# class Employee:
#     pass


# emp=Employee()
# em2=Employee()
# emp='lohit'

# em2='susumu terashi'
# print(emp)
# print(em2)

# print('________________________')
# # emp="Lohit"
# print(emp)

# print('________________________')


# class Person:
#     pass

# name=Person()
# email=Person()
# address=Person()
# phone=Person()

# name='New'
# print(name)



# class MyClass:
#       x = 5

# print(MyClass)

# print('_________________________')

# class MyClass:
#       x = 5

# p1 = MyClass()
# print(p1.x)


# The __init__() Function
# The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

# To understand the meaning of classes we have to understand the built-in __init__() function.

# All classes have a function called __init__(), which is always executed when the class is being initiated.

# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:


class Person:
    def __init__(self, name, age,email):
        self.name = name
        self.age = age
        self.email=email
    
p1 = Person("John", 36,'lohit2013n@gmail.com')


print('____________________________')
print(p1.name)
print(p1.age)
print(p1.email)



# Note: The __init__() function is called automatically every time the class is being used to create a new object.



