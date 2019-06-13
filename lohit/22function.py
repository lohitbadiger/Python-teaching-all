def greet(name="ryu" , time="morning"):
    print(f'Good morning {name} , what are you doing in the {time}')

# greet() its going to print name= ryu and time="mornig"
greet("loht", "assadsasd") #override the name nd time here??

greet("rek", "assafsfsddsasd") #override the name nd time here??
greet("sfdfdsfdloht", "fsfdassadsasd") #override the name nd time here??

print('------------------------------------------------------------')
greet()

greet()
greet()

# Python program to demonstrate 
# default arguments 
def myFun(x, y=50): 
    print("x: ", x) 
    print("y: ", y) 
  
# Driver code (We call myFun() with only 
# argument) 
myFun(10) 