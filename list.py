#list is mutable it can be change 
colors=['red','green','yellow','voilte','white']
print(type(colors))
print(colors)
print(colors[3])

#adding
colors.append("navyblue")
print(colors)
colors.insert(3,"blue")
print(colors)

#removing
colors.pop(1)
print(colors)
del colors[0]
print(colors)

#other method
print(colors.count("blue"))
colors.sort()
print(colors)

#cpoying list 1 to another
c1=colors.copy()
print(c1)
