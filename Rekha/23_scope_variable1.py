def print_message():  
    message = "hello !! I am going to print a message." # the variable message is local to the function itself  
    print(message)  
print_message()  
print(message) # this will cause an error since a local variable cannot be accessible here.   