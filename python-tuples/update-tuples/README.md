## Change Tuple Values 

once a tuple is created , toy cannot change its values , Tuplse are **unchangeable** , or 
**immutbale** as it also is called . 

But there is a workaround , You can convert the tuple into a list , change the list , and convert the list back inti a tuple 


for example : 

```

x = ('scania' , 'benz')
y = list(x)
y[0] = 'volvo'
x = tuple(y)

print(x)

```

## Add items 

Since tuples are immutable , they do not have a build-in **append()** method , but there are other ways to add items to a tuple . 

1.**Convert into a list** : Just like the workaround , you can convert it into a list , add you item(s) , and convert it back into a tuple .

for example : 

```

cars = ('volvo' , 'scania' , 'benz')

newCars = list(cars)
newCars.append('man')
cars = tuple(newCars)

print(cars)

```

