boxs=['lohit','rohit','mohit','ken']

for box in boxs:
    print('From this box',box)





print('____________________________________________')

# this is range in for loop

for x in range(2, 6):
      print('this is only the range', x) 

print('____________________________________________')






# this is range in for loop

for x in range(2, 30, 3):
      print("this will print", x) 

print('____________________________________________')



# This wil give range for 6 values and else statement after finsihed

for x in range(6):
      print(x)
else:
  print("Finally finished!")


print('____________________________________________')

# nested

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)







for i in range(3, 16, 3):
    quotient = i / 3
    print(f"{i} divided by 3 is {int(quotient)}.")


for i in range(len(captains)):
	    print(captains[i])