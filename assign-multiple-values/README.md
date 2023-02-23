## Many valuse to multiple varibales 

python allows you to assign valuse to multiple varibale in one line : 

```
x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)

```

**Note:** Make sure the number of variables matches the number of values, or else you will get an error.

## One value to multiple variables 

And you can assign the same value to multiple in on line : 

```
x = y = z = "Orange"
print(x)
print(y)
print(z)

```

## Unpack a collection 

if you have a collection of value in a list , tuple etc. Python allow you to extract the value into variables , This colled unpaking 


```
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

```