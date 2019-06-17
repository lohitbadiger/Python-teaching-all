# Object Methods
# Objects can also contain methods. Methods in objects are functions that belong to the object.

# Let us create a method in the Person class:


# Insert a function that prints a greeting, and execute it on the p1 object:


# class Person:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def myfunc(self):
#         print("Hello my name is " + self.name)

# p1 = Person("John", 36)
# p1.myfunc()






# class Person:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def myfunc(self):
#         print("Hello my name is " + self.name)

# p1 = Person("John", 36)
# p1.myfunc()

# print('___________________________________')

# class Good:

#     def __init__(self, dress, bad):
#         self.name = dress
#         self.age = bad
    
#     def myfunc(self):
#         print("Hello my name is " + self.name, self.age)

# lohit = Good("new dresss", "im Waering")
# lohit.myfunc()

# class Person1:
#     def __init__(mysillyobject, name, age):
#         mysillyobject.name = name
#         mysillyobject.age = age

#     def myfunc(abc):
#         print("Hello my name is " + abc.name)

# p1 = Person1("John", 36)
# p1.myfunc()




# Modify Object Properties
# You can modify properties on objects like this:
class Person:
    # instantiating the programs instances which holds the charcters/properties
    # Brain
    def __init__(self, name, age):
        self.name = name
        self.age = age


# enable the new method
# hand
    def myfunc(self):
        print("Hello my name is " + self.name)

# tasks
p1 = Person("John", 36)

# im assigning the new value to the age 
p1.age = 40

print(p1.age)



# Delete Object Properties
# You can delete properties on objects by using the del keyword:
class Person2:

    # property that person will contain
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person2("John", 36)

del p1.age

print(p1)
