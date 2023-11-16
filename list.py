'''
Basically the list is the array of Python. 

Definition: Lists are positionally orderd collections of arbitrarily typed objects 
and they also have no fixed size.

Unlike C, C++ or Java Python lists have no fixed type constraint.

'''

L = [123, "hello", 3.21]

#Slicing a list:
print(L[1:]) #Output: ['hello', 3.21]
print(L[:-1]) #Output: [123, 'hello']

L = L + [4, 5, 6] #i.e. [123, "hello", 3.21, 4, 5, 6]

print(L[-4:-1]) #Output: [3.21, 4, 5]

'''
List-specific operations:

'''
#Add object at the end of the list:
L.append("world") #i.e. [123, "hello", 3.21, 4, 5, 6, "world"]

#Delete object from the list
print(L.pop(2)) #Delete the object from list position L[2]

#Alternative for delete an object from a list.
del L[0]

#Add multiple items at the end of the list:
L.extend(["a","b","c"])

#Nesting
M = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

'''
List Comprehension Expression:

List comprehensions are coded in square brackets[].
'''
#Get the 2nd column from the matrix
print([row[1] for row in M]) #“Give me row[1] for each row in matrix M, in a new list.”

#Add 1 to each item in column 2
print([row[1] + 1 for row in M])

#Filter odd items
print([row[1] for row in M if row[1] % 2 == 0])

#Collect a diagonal from matrix
print([M[i][i] for i in [0, 1, 2]])

#Collect a diagonal from matrix
print([M[i][i] for i in [-1, -2, -3]])

print(list(range(5)))
print(list(range(-6, 5, 2)))
print([[x ** 2, x ** 3] for x in range(5)])
print([[x, x // 2, x * 2] for x in range(-6, 7, 2) if x > 0])

'''
Generators
'''
#Create a generator of row sums
G = (sum(row) for row in M)

#Iterating
print(next(G))
print(next(G))
print(next(G))

#The Build-in-function map()
print(list(map(sum, M)))

#Create a set of row sums
print({sum(row) for row in M})

#Create key : value table of row sums
print({i: sum(M[i]) for i in range(3)})

#print([i[j] for j in range(3) for i in M])