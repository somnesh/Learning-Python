'''
The tuple object is roughly like a list that cannot be changed.
Tuples are squences, like list, but they are immutable, like strings.

Functionally, they are used to represent fixed collection of items,

Syntactically, they are normally coded in parenthesis() instead to square brackets[].

'''

T = (1, 2, 3, 4, 4)

#Length
print(len(T))

#Concatenation 
print(T + (5, 6, 7))
print(T)

#Indexing, slicing, and more
print(T[0])

'''
Type-specific callable methods:
'''
print(T.index(4)) #The index method returns the index of a given value in the tuple if exists.
print(T.count(4)) #How many times a given value is appears in the tuple

#One-item tuples like the one here required a trailing comma
T = (2,) + T[1:]
print(T)

#Like lists and dictionaries, tuples support mixed types and nesting
T = 'hello', 2.0, [8, 9, 10] #The parenthesis enclosing a tuple`s item can usually be omitted, as done here

print(T) #output: ('hello', 2.0, [8, 9, 10])
print(T[1]) #output: 2.0
print(T[2][1]) #output: 9

