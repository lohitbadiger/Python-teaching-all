class employee:
    def __init__(self, first, last, sal):
        self.fname=first
        self.lname=last
        self.sal=sal
        self.email=first + '.' + last + '@company.com'
 
emp_1=employee('aayushi','johari',350000)
emp_2=employee('test','test',100000)
print(emp_1.email)
print(emp_2.email) 