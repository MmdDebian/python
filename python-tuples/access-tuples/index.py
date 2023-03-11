# the create parent tuple 

phones = ("apple" , 'samsung' , 'nokia')

# print indexes 

print(phones[0]) # output : apple


# refers to last item 
print(phones[-1]) # output : nokia 


# refers to second item 
print(phones[-2]) # output : samsung 


# create tuple with long items
cars = ('volvo' , 'scania' , 'benz' , 'mack' , 'daf' , 'man')


# specify negative indexes 
print(cars[-4:-1]) # output : ('benz' , 'mack' , 'daf')


# To determine if a specifyed item 
if 'volvo' in cars : 
    print('yes , volvo is in the cars tuple .')