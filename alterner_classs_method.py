class Emp:
    emp_count=8
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def printitng(self):
        return f"name is {self.name} and age is {self.age}"

    @classmethod                    
    def changeemp(cls,newemp):
        cls.emp_count=newemp

    @classmethod                    #alternative constructor class method 
    def alternetstring(cls,string):
        data=string.split("-")
        return cls(data[0],data[1])

object1=Emp('rohit',18)
print(object1.printitng())

object2=Emp.alternetstring("ajay--18")
print(object2.printitng())