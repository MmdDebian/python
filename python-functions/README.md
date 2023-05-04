# Python functions 

A function is a block of code which only runs when it is colled.

You can pass data , known as parameters , into a function . 

A function can return data as a result .


# Creating a function 
In python a function is defined using the **def** keyword :

```
def message():
    print('hello there')

```

# Calling a function 
To call a function , use the function name followed by parenthesis:

```

def my_func():
    print('called function')


my_func()

```

# Arguments

Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:


```
def my_function(fname):
  print(fname + " Refsnes")

my_function("ali")
my_function("hassan")
my_function("hadi")

```

# Number of Arguments
By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.

```
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

```


if you try to call rhe function with  or  arguments , you will get an error : 


```

def my_function(fname , lname):
    print(fname + ' ' + lname)


my_function('mohamad') # error 

```


## Arbitrary Arguments, ***args**


If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:


```

def my_function(*kids):
  print('The youngest child is ' + kids[2])


my_function('milad' , 'mamad' , 'ali')

```

## Keyword Arguments

You can also send arguments with the key = value syntax . 

This way the order of the argumenrs does not matter .

```

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

```


