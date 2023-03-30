## Python Loops 

Python has two primitve loop commands 

* **while** Loops 
* **for** Loops 

## The while loop 

With the **while** loop we can execute a set of statements as long as a condation is true .

```

i = 1
while i < 6:
  print(i)
  i += 1

```

**Note: remember to increment i, or else the loop will continue forever.**

The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.

## The break statement 

With the **break** statement we can stop the loop even if the while condation is true . 

```
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

```

## The continue statement 

with the **continue** statement we can stop the current iteration , and continue with the nest: 

```
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

```

## The Else statement 

With the else statement we can run a block of code once when the condition no longer is true:

``` 
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

```