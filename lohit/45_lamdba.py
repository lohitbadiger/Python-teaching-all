# if im using function only one time no need to cl dem again and again
# so we can define dos kind of function as Lamda

num=[1,2,3,45,6,7,8,9]


def sqrt(n):
    return n*n

# using lamba

#lambda are inline functions
# used wen perticular fucntion need to be run @ only one , 
# can be used time with map or inline functions
print(list(map(lambda n: n*n , num)))

