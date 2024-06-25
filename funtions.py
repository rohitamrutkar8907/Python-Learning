"""'def addinng(a,b):   # note:after funtion dec spce require to new line cause of no bracker in python
    print(a+b)

addinng(10,20)  #calling funtion"""

#funtion iside funtion
def greater(a,b,c):
    if a>b and a>c:
        print("a is gretest")
    elif b>a and b>c:
        print("b is greatest")
    else :
        print("c is gratest")    
greater(20,78,6)       
      
#funtion inside funtion
def  d1():
    s="hello"
    def d2():
        print(s)
    d2()
d1()    