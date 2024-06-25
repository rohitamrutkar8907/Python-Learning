def a(fun):
        def c():
            print("Rohit")
            fun()
            print("have a nice day")
        return c        
@a #b=a(b)
def b():
    print("good morning")

b()
