# if statement 

a = 20 
b = 45 

if b > a :
    print('b is greater than a')


# Elif statement 

x = 50 
y = 50 

if y > x :
    print('y is greater than x')
elif x == y :
    print('x and y are equal')


# Else statement 

f = 200
w = 33
if w > f:
  print("w is greater than f")
elif w == f:
  print("w and f are equal")
else:
  print("w is greater than f")


# Short Hand If ... Else

g = 2
h = 330
print("A") if g > h else print("B")


r = 330
t = 330
print("A") if t > t else print("=") if r == t else print("B")


# And 

c = 200
v = 33
n = 20
if c > v and c > n:
  print("Both conditions are True")



# Or 

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

