def area(radius):
    print(3.142* radius * radius)


area(4)

# Pass by Reference
# Here x is a new reference to same list lst 
def myFun(x): 
    x[0] = 20

# Driver Code (Note that lst is modified 
# after function call. 
lst = [10, 11, 12, 13, 14, 15] 
myFun(lst)
print(lst) 
print('_____________________link broken___________________________________')

def myFun2(x): 
  
   # After below line link of x with previous 
   # object gets broken. A new object is assigned 
   # to x. 
   x = [20, 30, 40] 
  
# Driver Code (Note that lst is not modified 
# after function call. 
lst = [10, 11, 12, 13, 14, 15]  
myFun2(lst); 
print(lst) 

def myFun(x): 
  
   # After below line link of x with previous 
   # object gets broken. A new object is assigned 
   # to x. 
   x = 20
  
# Driver Code (Note that lst is not modified 
# after function call. 
x = 10 
myFun(x); 
print(x)  


# Variable length arguments:
# We can have both normal and keyword variable number of arguments. Please see this for details.


# Python program to illustrate   
# *args for variable number of arguments 
def myFun(*argv):  
    for arg in argv:  
        print (arg) 
    
myFun('Hello', 'Welcome', 'to', 'spcieup sussu')  








def swap(x, y): 
    temp = x; 
    x = y; 
    y = temp; 
  
# Driver code 

x = 2
y = 3
swap(y,x) 
print(y) 
print(x) 
