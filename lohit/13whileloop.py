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