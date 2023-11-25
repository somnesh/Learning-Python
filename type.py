'''
The type object, returned by the 'type' build-in function, is an object that gives the type of another object.

'''
L = [1, 2, 3, 4]

print(type(L)) #output: <class 'list'>
print(type(type(L))) #output: <class 'type'>

'''
The type object in it's most practical application allows code to check the types of the objects it processes.

'''
if type(L) == type([]): #Type testing
    print("Yes")

if type(L) == list: #Using the type name
    print("Yes")

if isinstance(L, list): #Object-oriented tests
    print("Yes")