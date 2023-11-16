'''
A dictionary is used to store {key : value} pairs

Here some way to crate a dictionary

'''
#method 1:
person1 = {"name" : "A", "age" : "31", "occupation" : "Businessman"}

#method 2:
person2 = {}
person2["name"] = "B"
person2["age"] = "25"
person2["occupation"] = "Serviceman"

#method 3:
person3 = dict(name = "C", age = "20", occupation  = "Student")

#method 4:
person4 = dict(zip(["name", "age", "occupation"],["D", "45", "Teacher"]))


print(person1)
print(person2)
print(person3)
print(person4)

'''
Python`s object nesting

'''

record = {
    "name" : {"first" : "Somnesh", "last" : "Mukhopadhyay"},
    "jobs" : ["dev", "Student"],
    "age" : 20
}

print(record)

#We can access the last name as follows:
print(record["name"]["last"])

#Just like that we can access jobs as follows:
print(record["jobs"][1])

#Because the "jobs" is a list in type we can add another 'job post' using append.
record["jobs"].append("Singer")

print(record["jobs"])

#We can retrive the keys of a dictionary items as follows:
test_dict = {"a" : 1, "c" : 3, "b" : 2}

#Returns a object that contains the keys.
keys = test_dict.keys()

#We can convert it into a list to play with it like sorting the keys etc.
keys = list(keys)
keys = keys.sort()

#The build-in-function 'sorted' does exactly the same as we did before 
for key in sorted(test_dict):
    print(key ,"=>", test_dict[key])

