# create tparent tuple 

# update item with workaround convert tuple into list :
cars = ('volvo' , 'scania' , 'benz')

convert = list(cars)
convert[0] = 'fh500'
cars = tuple(convert)

print(cars)


# add item with workaround convert tuple into list :
addItem = list(cars)
addItem.append('man')
cars = tuple(addItem)


print(cars)