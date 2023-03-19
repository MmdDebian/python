# create Python Dictionaries

adminUser = {
    "name" : "mohamad",
    "username" : "mohamad",
    "email" : "mohamad@gmail.com",
}

print(adminUser)

# use items 

print(adminUser['name']) # output : mohamad


# dictionary items - daya type 

# The values in dictionaries items can be of any data type :

product = {
    "name" : "apple",
    "size" : 250 ,
    "color" : ["red" , "blue","white"],
    "available" : True 
} 

# chack item [True or False]
if product['available']:
    print('yse' , 'Yes, this product is available')

# print dictionary item :
for color in product['color'] : 
    print(color)

