# normal variable 

message = 'hello all , this messsage for test '



# define global value : 

def isAdmin():
    global isAdmin 
    username = input('Enter the username : \n')
    
    if username == 'mohamad' : 
        isAdmin = True 
    else:
        isAdmin = False 
    
    return isAdmin


print(isAdmin())