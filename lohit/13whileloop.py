age=20

num=0
 

while num<age:
        
    if num==0:
        num+=1
        continue #from here it will go while num<age line
        
    if num %2 ==0:
        print(num)
    
    if num>10:
        break
    
    num+=1

# Program to add natural
# numbers upto 
# sum = 1+2+3+...+n

# To take input from the user,
# n = int(input("Enter n: "))

n = 10

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum)

xyz=5
while xyz>0:
    n-=1
    print(xyz)

n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('Loop ended.')

n = 5
while n > 0:
    n -= 1
    print(n)
    if n == 2:
        break
    else:
        print('Loop done.')
