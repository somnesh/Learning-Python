# Introducing Python Object Types

In Python, data takes the form of objects — either built-in objects that Python provides, or objects we create using Python classes.

## Python’s Core Data Types

Python’s built-in object types and some of the syntax used to code their literals — that is, the expressions that generate these objects. Some of these types will probably seem familiar if you’ve used other languages; for instance, numbers and strings represent numeric and textual values, respectively, and file objects provide an interface for processing real files stored on your computer.  

#### Table: Built-in objects preview[^bignote] 
| Object type | Example literals/creation |
|-------------|---------------------------|
| Numbers | `1234`, `3.1415`, `3+4j`, `0b111`, `Decimal()`, `Fraction()` |
| Strings | `'spam'`, `"Bob's"`, `b'a\x01c'`, `u'sp\xc4m'` |
| Lists | `[1, [2, 'three'], 4.5]`, `list(range(10))` |
| Dictionaries | `{'food': 'spam', 'taste': 'yum'}`, `dict(hours=10)` |
| Tuples | `(1, 'spam', 4, 'U')`, `tuple('spam')`, `namedtuple` |
| Files | `open('eggs.txt')`, `open(r'C:\ham.bin', 'wb')` |
| Sets | `set('abc')`, `{'a', 'b', 'c'}` |
| Other core types | `Booleans`, `types`, `None` |
| Program unit types | `Functions`, `modules`, `classes` |
| Implementation-related types | `Compiled code`, `stack tracebacks` |  

>*Program units* such as functions, modules, and classes — are objects in Python too; they are created with statements and expressions such as `def`, `class`, `import`, and `lambda` and may be passed around scripts freely, stored within other objects, and so on.  
>
>Python also provides a set of *implementation-related types* such as compiled code objects, which are generally of interest to tool builders more than application developers; we’ll explore these in later parts too, though in less depth due to their specialized roles.

[^bignote]: This *Table* isn't really complete, because everything we process in Python programs is a kind of object. For instance, when we perform text pattern matching in Python, we create pattern objects.

We’ll study each of the object types in the above *Table* in detail in upcoming chapters. Before digging into the details, though, let’s begin by taking a quick look at Python’s core objects in action.  

## Numbers

If you’ve done any programming or scripting in the past, some of the object types in the given *Table* will probably seem familiar. Even if you haven’t, numbers are fairly straight forward. Python’s core objects set includes the usual suspects: integers that have no fractional part, floating-point numbers that do, and more exotic types — complex numbers with imaginary parts,  decimals with fixed precision, rationals with numerator and denominator, and full-featured sets. Built-in numbers are enough to represent most numeric quantities—from your age to your bank balance — but more types are available as third-party add-ons.  

Although it offers some fancier options, Python’s basic number types are, well, basic. Numbers in Python support the normal mathematical operations. For instance, the plus sign `+` performs addition, a star `*` is used for multiplication, and two stars `**` are used for exponentiation:

```python
# Integer addition
print(123 + 222) # Output: 345

# Floating point multiplication
print(1.5 * 4) # Output: 6.0

# 2 to the power 100
print(2 ** 100) # Output: 1267650600228229401496703205376
```

>Notice the last result here: Python 3.X’s integer type automatically provides extra precision for large numbers like this when needed.  

Besides expressions, there are a handful of useful numeric modules that ship with Python—modules are just packages of additional tools that we import to use:  

```python
import math

print(math.pi) # Output: 3.141592653589793

print(math.sqrt(85)) # Output: 9.219544457292887

```  

The math module contains more advanced numeric tools as functions, while the random module performs random-number generation and random selections:

```python
import random

print(random.random()) # Output: 0.4149023916060619 (again, random!)

print(random.choice([1, 2, 3, 4])) # Output: 1
```  

Python also includes more exotic numeric objects — such as complex, fixed-precision, and rational numbers, as well as sets and Booleans — and the third-party open source extension domain has even more (e.g., matrixes and vectors, and extended precision numbers). We’ll defer discussion of these types later.

## Strings

Strings are used to record both textual information (your name, for instance) as well as arbitrary collections of bytes (such as an image file’s contents). They are our first example of what in Python we call a sequence — a positionally ordered collection of other objects. Sequences maintain a left-to-right order among the items they contain: their items are stored and fetched by their relative positions. Strictly speaking, strings are sequences of one-character strings; other, more general sequence types include lists and tuples, covered later.  

### Sequence Operations

As sequences, strings support operations that assume a positional ordering among items. For example, if we have a four-character string coded inside quotes, we can verify its length with the built-in len function and fetch its components with indexing expressions:

```python
# Make a 5-character string, and assign it to a name
s = 'hello'

print(len(s)) # Output: 5

# The first item in s
print(s[0]) # Output: 'h'

# The second item in s, from left
print(s[1]) # Output: 'e'
```  

In Python, we can also index backward, from the end — positive indexes count from the left, and negative indexes count back from the right:

```python
# The last item from the end in s
print(s[-1]) # Output: 'o'

# The second-last item from the end
print(s[-2]) # Output: 'l'

```  

In addition to simple positional indexing, sequences also support a more general form of indexing known as *slicing*, which is a way to extract an entire section (slice) in a single step. For example:

```python
print(s) # Output: 'world'

print(s[1:3]) # Output: 'or' 

# That is, s[1] to s[2]
```
>Their general form, `X[I:J]`, means “give me everything in `X` from offset `I` up to but not including offset `J`. The result is returned in a new object.  

In a slice, the left bound defaults to zero, and the right bound defaults to the length of the sequence being sliced. This leads to some common usage variations:

```python
print(s[1:]) # Output: 'orld'

print(s[0:3]) # Output: 'wor'

print(s[:3]) # Output: 'wor'

print(s[:-1]) # Output: 'worl'

print(s[:]) # Output: 'world'
```  

Finally, as sequences, strings also support concatenation with the plus sign and *repetition*:

```python
print(s + 'xyz') # Output: 'worldxyz'

# s is unchanged
print(s) # Output: 'world'

print(s * 3) # Output: 'worldworldworld'
```  

### Immutability

Notice in the prior examples that we were not changing the original string with any of the operations we ran on it. Every string operation is defined to produce a new string as its result, because strings are immutable in Python — they cannot be changed in place after they are created.

```python

print(s) # Output: 'world'

s[0] = 'a' # immutable objects cannot be changed

# Error: 
# s[0] = 'a'
# TypeError: 'str' object does not support item assignment

new_s = 'a' + s[1:] # But we can run expressions to make new objects

print(new_s) # Output: 'aorld'
```  

Every object in Python is classified as either immutable (unchangeable) or not. In terms of the core types, `numbers`, `strings`, and `tuples` are `immutable`; `lists`, `dictionaries`, and `sets` are not — they can be changed in place freely.

Strictly speaking, you can change text-based data in place if you either expand it into a `list` of individual characters and join it back together with nothing between, or use the newer `bytearray` type available in Pythons 2.6, 3.0, and later:

```python
s = 'hello'
l = list(s) # Expanding to a list

print(l) # Output: ['h', 'e', 'l', 'l', 'o']

l[0] = 'j' # Change in place

# Join with empty delimeter
print(''.join(l)) # Output: jello

B = bytearray(b'fish') # A byte/list hybrid
B.extend(b'eggs')

print(B) # Output: bytearray(b'fisheggs')

print(B.decode()) # Output: fisheggs
```

>The `bytearray` supports in-place changes for text, but only for text whose characters are all at most 8-bits wide (e.g., ASCII). All other strings are still immutable.  

### Type-Specific Methods

Every string operation we’ve studied so far is really a sequence operation — that is, these operations will work on other sequences in Python as well, including lists and tuples. In addition to generic sequence operations, though, strings also have operations all their own, available as methods — functions that are attached to and act upon a specific object, which are triggered with a call expression.  

For example, the string `find` method is the basic substring search operation, and the string `replace` method performs global searches and replacements; both act on the subject that they are attached to and called from:

```py
s = 'World'

print(s.find('or')) # Output: 1
print(s.find('ld')) # Output: 3

print(s.replace('or','ABC')) # Output: WABCld
print(s) # Output: World
```  
Again, despite the names of these string methods, we are not changing the original strings here, but creating new strings as the results—because strings are immutable.  

Other methods split a string into substrings on a delimiter, perform case conversions, test the content of the string, and strip whitespace characters off the ends of the string:

```py
line = 'aaa,bbb,cccc,dd'

# Split on a delimiter into a list of substrings.
print(line.split(',')) # Output: ['aaa', 'bbb', 'cccc', 'dd']

# Upper and lower case conversion
s = 'abcd'
print(s.upper()) # Output: ABCD

# content tests: isalpha(), isdigit(), etc.
print(s.isalpha()) # Output: True

# Remove whitespace characters on the right side
line = 'aaa,bbb,cccc,dd\n'
print(line.rstrip()) # Output: 'aaa,bbb,cccc,dd'

# Combine two operations
print(line.rstrip().split(',')) # Output: ['aaa', 'bbb', 'ccccc', 'dd']
```  

>Notice the last command here — it strips before it splits because Python runs from left to right, making a temporary result along the way.

Strings also support an advanced substitution operation known as *formatting*, available as both an expression and a string method call:

```py
# Formatting expression
print('%s, xyz, and %s' %('ABC','abc')) # Output: ABC, xyz, and abc

# Formatting method
print('{0}, xyz, and {1}'.format('ABC', 'abc!')) # Output: ABC, xyz, and abc!

# Numbers optional
print('{}, xyz, and {}'.format('ABC', 'abc!')) # Output: ABC, xyz, and abc!

# Formatting numbers
# Separetors, decimal digits
print('{:,.2f}'.format(296999.2567)) # Output: 296,999.26

# Digits, padding, signs
print('%.2f | %+05d' % (3.14159, −42)) # Output: 3.14 | -0042
```  

### Unicode Strings

Python’s strings also come with full Unicode support required for processing text in internationalized character sets. In Python 3.X, the normal str string handles Unicode text (including ASCII) a distinct `bytes` string type represents raw byte values:

```py
# Normal str strings
print('sp\xc4m') # Output: spÄm

# Byte string
print(b'a\x01c') # Output: b'a\x01c'

# Unicode literal
print(u'sp\u00c4m') # Output: spÄm
```

## Lists

The Python `list` object is the most general sequence provided by the language. Lists are positionally ordered collections of arbitrarily typed objects, and they have no fixed size. They are also mutable — unlike strings, lists can be modified in place by assignment to offsets as well as a variety of list method calls. Accordingly, they provide a very flexible tool for representing arbitrary collections.

Unlike C, C++ or Java Python lists have no fixed type constraint.

### Sequence Operations

Because they are sequences, lists support all the sequence operations we discussed for strings:

```python
L = [123, "hello", 3.21]

#Slicing a list:
print(L[1:]) #Output: ['hello', 3.21]
print(L[:-1]) #Output: [123, 'hello']

L = L + [4, 5, 6] #i.e. [123, "hello", 3.21, 4, 5, 6]

print(L[-4:-1]) #Output: [3.21, 4, 5]
```

### List-specific operations:

Lists have no fixed size. That is, they can grow and shrink on demand, in response to list-specific operations:

```py
#Add object at the end of the list:
L.append("world") #i.e. [123, "hello", 3.21, 4, 5, 6, "world"]

#Delete the object from list position L[2]
print(L.pop(2)) # Output: 3.21

#Alternative for delete an object from a list.
del L[0]
print(L) # Output: ['hello', 4, 5, 6, 'world']

#Add multiple items at the end of the list:
L.extend(["a","b","c"])
print(L) # Output: ['hello', 4, 5, 6, 'world', 'a', 'b', 'c']

#Nesting
M = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```
Here, the list `append` method expands the list’s size and inserts an item at the end; the `pop` method (or an equivalent `del` statement) then removes an item at a given offset, causing the list to shrink.  

Other list methods insert an item at an arbitrary position (`insert`), remove a given item by value (`remove`), add multiple items at the end (`extend`), and so on.  

Because lists are mutable, most list methods also change the list object in place, instead of creating a new one:

```py
l = ['bb', 'aa', 'cc']
l.sort()
print(l) # Output:  ['aa', 'bb', 'cc']

l.reverse()
print(l) # Output:  ['cc', 'bb', 'aa']
```
The list `sort` method here, for example, orders the list in ascending fashion by default, and `reverse` reverses it—in both cases, the methods modify the list *directly*.

### List Comprehension Expression:

In addition to sequence operations and list methods, Python includes a more advanced operation known as a *list comprehension expression*.

```py
#Get the 2nd column from the matrix
#“Give me row[1] for each row in matrix M, in a new list.”
print([row[1] for row in M]) # Output: [2, 5, 8]

#Add 1 to each item in column 2
print([row[1] + 1 for row in M]) # Output: [3, 6, 9]

#Filter odd items
print([row[1] for row in M if row[1] % 2 == 0]) # Output: [2, 8]

#Collect a diagonal from matrix
print([M[i][i] for i in [0, 1, 2]]) # Output: [1, 5, 9]

#Collect a diagonal from matrix
print([M[i][i] for i in [-1, -2, -3]]) # Output: [9, 5, 1]

print(list(range(5))) # Output: [0, 1, 2, 3, 4]

print(list(range(-6, 5, 2))) # Output: [-6, -4, -2, 0, 2, 4]

print([[x ** 2, x ** 3] for x in range(5)]) # Output: [[0, 0], [1, 1], [4, 8], [9, 27], [16, 64]]

print([[x, x // 2, x * 2] for x in range(-6, 7, 2) if x > 0]) # Output: [[2, 1, 4], [4, 2, 8], [6, 3, 12]]
```

### Generators

```py
#Create a generator of row sums
G = (sum(row) for row in M)

#Iterating
print(next(G)) # Output: 6
print(next(G)) # Output: 15
print(next(G)) # Output: 24

#The Build-in-function map()
print(list(map(sum, M))) # Output: [6, 15, 24]

#Create a set of row sums
print({sum(row) for row in M}) # Output: {24, 6, 15}

#Create key : value table of row sums
print({i: sum(M[i]) for i in range(3)}) # Output: {0: 6, 1: 15, 2: 24}

#print([i[j] for j in range(3) for i in M]) # Output: [1, 4, 7, 2, 5, 8, 3, 6, 9]
```

## Dictionaries

Python dictionaries are something completely different — they are not sequences at all, but are instead known as mappings. Mappings are also collections of other objects, but they store objects by key instead of by relative position. In fact, mappings don’t maintain any reliable left-to-right order; they simply map keys to associated values. Dictionary are coded in curly braces and consist of a series of {key : value} pairs.  

Here are some way to crate a dictionary:

```py
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


print(person1) # Output: {'name': 'A', 'age': '31', 'occupation': 'Businessman'}
print(person2) # Output: {'name': 'B', 'age': '25', 'occupation': 'Serviceman'}
print(person3) # Output: {'name': 'C', 'age': '20', 'occupation': 'Student'}
print(person4) # Output: {'name': 'D', 'age': '45', 'occupation': 'Teacher'}
```

### Nesting

Suppose, though, that the information is more complex. Perhaps we need to record a first name and a last name, along with multiple job titles. This leads to another application of Python’s object nesting in action.

```py
record = {
    "name" : {"first" : "Somnesh", "last" : "Mukhopadhyay"},
    "jobs" : ["dev", "Student"],
    "age" : 20
}

print(record) # Output: {'name': {'first': 'Somnesh', 'last': 'Mukhopadhyay'}, 'jobs': ['dev', 'Student'], 'age': 20}

#We can access the last name as follows:
print(record["name"]["last"]) # Output: Mukhopadhyay

#Just like that we can access jobs as follows:
print(record["jobs"][1]) # Output: Student

#Because the "jobs" is a list in type we can add another 'job post' using append.
record["jobs"].append("Singer")

print(record["jobs"]) # Output: ['dev', 'Student', 'Singer']
```

### Sorting Keys: for Loops

As mentioned earlier, because dictionaries are not sequences, they don’t maintain any dependable left-to-right order. If we make a dictionary and print it back, its keys may come back in a different order than that in which we typed them, and may vary per Python version and other variables:

```py
#We can retrive the keys of a dictionary items as follows:
test_dict = {"a" : 1, "c" : 3, "b" : 2}

#Returns a object that contains the keys.
keys = test_dict.keys()

#We can convert it into a list to play with it like sorting the keys etc.
keys = list(keys)
keys = keys.sort()

for key in keys:
    print(key ,"=>", test_dict[key])

# Output: 
# a => 1
# b => 2
# c => 3
```

This is a three-step process, although, as we’ll see in later chapters, in recent versions of Python it can be done in one step with the newer `sorted` built-in function. The `sorted` call returns the result and sorts a variety of object types, in this case sorting dictionary keys automatically:

```py
#The build-in-function 'sorted' does exactly the same as we did before 
for key in sorted(test_dict):
    print(key ,"=>", test_dict[key])

# Output: 
# a => 1
# b => 2
# c => 3
```