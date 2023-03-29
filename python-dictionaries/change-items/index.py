car = {
    "brand" : "volvo" , 
    "model" : "fh" , 
    "year" : 2018 
}

# use item for update 
 
car["year"] = 2023 

print(car) 



# use update method for change item
newCar = {
    "brand" : "scania",
    "model" : "470 top line" , 
    "year" : 2017
}

newCar.update({"year" : 2023})

print(newCar)