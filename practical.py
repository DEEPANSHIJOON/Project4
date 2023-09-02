class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # add two objects
    def __add__(self, other):
        return self.real + other.real, self.imag + other.imag

obj1 = Complex(1, 2)
obj2 = Complex(3, 4)
obj3 = obj1 + obj2
print(obj3)

# Output: (4, 6)
class Employee:

    def message(self):
        print('This message is from Employee')

class Department(Employee):

    def message(self):
        print('This Department is inherited from Employee')

class Sales(Department):

    def message(self):
        print('This Sales is inherited from Employee')

emp = Employee()
emp.message()

print('------------')
dept = Department()
dept.message()

print('------------')
sl = Sales()
sl.message()