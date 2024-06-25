number =[1,2,3,4,5,6]
a=list(map(lambda n:n*n,number))
print(a)

a=list(filter(lambda n:n%2==0,number))
print(a)