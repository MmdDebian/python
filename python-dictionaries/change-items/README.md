## Change dictionary items 

you can change the value of a specific item by referring to its key name : 


```

car = {
    "brand" : "volvo",
    "model" : "FH",
    "year" : 1964
}

car["year"] = 2023

```

## Update dictionary 

The **update()** method will update the dictionary with the items from the given argument.

The argument must be a dictionary , or in iterable object with **key:value** pairs.


```

car = {
    "brand" : "scania",
    "model" : "470 Top line" , 
    "year" : 2018 
}

car.update({"year" : 2023})

```