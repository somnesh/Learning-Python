# Introducing Python Object Types

In Python, data takes the form of objects—either built-in objects that Python provides, or objects we create using Python classes.

## Python’s Core Data Types

Python’s built-in object types and some of the syntax used to code their literals—that is, the expressions that generate these objects. Some of these types will probably seem familiar if you’ve used other languages; for instance, numbers and strings represent numeric and textual values, respectively, and file objects provide an interface for processing real files stored on your computer.  

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
| Program unit types[^bignote] | `Functions`, `modules`, `classes` |
| Implementation-related types | `Compiled code`, `stack tracebacks` |

[^bignote]: *Program units* such as functions, modules, and classes — are objects in Python too; they are created with statements and expressions such as `def`, `class`, `import`, and `lambda` and may be passed around scripts freely, stored within other objects, and so on.  

