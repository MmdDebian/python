# For loops 

for name in ['milad','erfan','mahdi']:
    print(name)


# Looping Through a String

for x in 'mohamad':
    print(x)


# The break Statement
cars = ["volvo", "scania", "benz"]
for car in cars:
  print(car)
  if car == "scania":
    break


# The continue Statement 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


# The range() Function 
for x in range(6):
   print(x)



# Nested Loops 
colors = ["red", "big", "tasty"]
cars = ["volvo", "man", "benz"]

for color in colors:
  for car in cars:
    print(color,car)


# The pass Statement 
for x in [0, 1, 2]:
  pass