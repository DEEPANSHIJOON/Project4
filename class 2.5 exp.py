# a. Write a python program to demonstrate and define a class and object.
class abc():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def prnt(self):
        print(self.a)
        print(self.b)


x=abc(10,15)
x.prnt()

# b. Write a python program to create employee class with some attributes and methods.
class employee():
    count=0
    def __init__(self,name,uid,salary):
        self.name=name
        self.uid=uid
        self.salary=salary
        employee.count+=1
    def prnt(self):
        print(self.name)
        print(self.uid)
        print(self.salary)
emp1=employee("rahul","22MAI14008",35000)
emp2=employee("aman","22MAI14007",55000)
emp3=employee("ashish","22MAI14004",25000)
emp1.prnt()
emp2.prnt()
emp3.prnt()
print(employee.count)


# c. Write a python program to implement operator overloading.
class operation():
    def __init__(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
    def __add__(self):
        return self.a+self.b
    def __sub__(self):
        return self.d-self.c
op=operation(4,5,6,7)
print(op.__add__())

print(op.__sub__())


