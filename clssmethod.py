class Emp:
    emp_count=8
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def printitng(self):
        return f"name is {self.name} and age is {self.age}"

    @classmethod                    #conver funtion into class method
    def changeemp(cls,newemp):
        cls.emp_count=newemp

'''
object1=Emp('rohit',18)
print(object1.printitng())

object1.emp_count=12                #instace variable... this obj create its own variable
print(object1.emp_count)


print(Emp.emp_count)                #class variable is able to change main vrible value
Emp.emp_count=25 
print(Emp.emp_count)
'''
rohit=Emp('a',12)
print(rohit.emp_count)
rohit.changeemp(25)
print(rohit.emp_count)
print(Emp.emp_count)


