A={'Age':25, 'Name':'rekha'}

print(A)

print(A['Age'])

print(A['Name'])

















# Creating an empty Dictionary 
Dict = {} 
print("Empty Dictionary: ") 
print(Dict) 

# Creating a Dictionary 
# with Integer Keys 
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'} 
print("\nDictionary with the use of Integer Keys: ") 
print(Dict) 

# Creating a Dictionary 
# with Mixed keys 
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]} 
print("\nDictionary with the use of Mixed Keys: ") 
print(Dict) 

# Creating a Dictionary 
# with dict() method 
Dict = dict({1: 'Geeks', 2: 'For', 3:'Geeks'}) 
print("\nDictionary with the use of dict(): ") 
print(Dict) 

# Creating a Dictionary 
# with each item as a Pair 
Dict = dict([(1, 'Geeks'), (2, 'For')]) 
print("\nDictionary with each item as a pair: ") 
print(Dict) 













print('----------------------------------')





# {1: 'Geeks', 2: 'For'}# Creating an empty Dictionary 
Dict = {} 
print("Empty Dictionary: ") 
print(Dict) 

# Adding elements one at a time 
Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ") 
print(Dict) 

# Adding set of values 
# to a single Key 
Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ") 
print(Dict) 

# Updating existing Key's Value 
Dict[2] = 'Welcome'
print("\nUpdated key value: ") 
print(Dict) 

# Adding Nested Key value to Dictionary 
Dict[5] = {'Nested' :{'1' : 'Life', '2' : 'Geeks'}} 
print("\nAdding a Nested Key: ") 
print(Dict) 




print('----------------------------------')
# Python program to demonstrate 
# accesing a element from a Dictionary 

# Creating a Dictionary 
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'} 

# accessing a element using key 
print("Acessing a element using key:") 
print(Dict['name']) 

# accessing a element using key 
print("Acessing a element using key:") 
print(Dict[1]) 

# accessing a element using get() 
# method 
print("Acessing a element using get:") 
print(Dict.get(3)) 
