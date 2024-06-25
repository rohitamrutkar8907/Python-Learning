#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
dic={
    '1':'a',
    '2':'b',
    '3':'c',
    '4':'d',
    "colors":["red", "white", "blue"]
    }


    #accessing
print(dic)
print(dic['1'])
print(dic.get('colors'))
print(dic.keys())       #get all key of dictionary
print(dic.values())       #get all value of dictionary


#changing or updatee
dic['1']='z'
dic.update({"2":"v"})
print(dic)


"""

Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary"""