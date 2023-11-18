'''
Sets are unorderd collection of unique and immutable objects.

'''
X = set('spam')
print(X)

Y = {'i', 'm', 'k'}
print(Y)

print(X,Y)

print(X & Y) #Intersection

print(X | Y) #Union

print(X - Y) #Difference

print(X > Y) #Superset

print({n ** 2 for n in [1, 2, 3, 4]}) #Set comprehensions

#Filtering out duplicates:
print(list(set([1, 2, 4, 2, 5, 6, 2, 1, 7, 3])))

#Finding differences in collections:
print(set('spam') - set('ham'))

#Order-neutral equality tests:
print(set('spam') == set('asmp'))