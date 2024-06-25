'''n=int(input("enteer no==>"))
def fibonacci():
    a=0
    b=1
    if n==1:
        print(a)
    elif n==2:
        print(a,b)
    else:
        print(a,b, end =" ")
        for i in range(n-2):
            c=a+b
            a=b
            b=c
            print(b, end =" ")
fibonacci()           


#2nd way
a=int(input("Enter the terms"))
f=0                                         #first element of series
s=1                                         #second element of series
if a<=0:
    print("The requested series is",f)
else:
    print(f,s,end=" ")
    for x in range(2,a):
        next=f+s                           
        print(next,end=" ")
        f=s
        s=next'''



def d1():
     n=int(input("enter number-->"))
     x=0
     y=1
     z=0
     while z<=n:
         print(z)
         x=y
         y=z
         z=x+y
d1()