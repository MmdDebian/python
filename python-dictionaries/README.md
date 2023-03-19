```
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

```

## Dictionary

Dictionaries are used to store data value in **key:value** pairs .

A dictionaries is a collcetion witch is orderd* . changeable and do not allow duplicates.

**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.**

Dictionaries are written with curly brackets, and have keys and values:
```
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

```

## Dictionary Items

Dictionary items are ordered, changeable, and does not allow duplicates.

Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

```

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

```

## Ordered or Unordered?

**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.**

When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.

## Changeable

Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

## Duplicates Not Allowed

Dictionaries cannot have two items with the same key:

```
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

```

## Dictionary Length

To determine how many items a dictionary has, use the **len()** function:

```
print(len(thisdict))

```

## Dictionary Items - Data Types

The values in dictionary items can be of any data type:

```
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

```

* **List** is a collection which is ordered and changeable. Allows duplicate members.
* **Tuple** is a collection which is ordered and unchangeable. Allows duplicate members.
* **Set** is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
* **Dictionary** is a collection which is ordered** and changeable. No duplicate members.