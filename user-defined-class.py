'''
Classes define new types of objects that extend the core set, so they merit a passing glance here.
Although there is no such specific core type in Python.

'''
class Worker:
    def __init__(self, name, pay) -> None: # Initialize when created
        self.name = name # self is the new object
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1] # Split string on blanks
    
    def givenRaise(self, percent):
        self.pay *= (1.0 + percent)

person1 = Worker('John Don', 5000)
person2 = Worker('Papa Player', 6000)

print(person1.lastName())
person1.givenRaise(.10)

print(person1.pay)