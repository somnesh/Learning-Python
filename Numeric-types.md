
# Numeric Types

In Python, numbers are not a single object type, but a category of similer types.
Python supports the usual numeric types (integers and floating points), as well as literals for creating 
numbers and expressions for processing them. In addition, Python provides more advanced numeric programming
support and objects for more advanced work.

**A complete inventory of Python's numeric toolbox includes:**

- Integer and floating-point objects
- Complex number objects
- Decimal: fixed precision objects
- Fraction: rational number objects
- Sets: collections with numeric operations
- Booleans: true and false
- Build-in functions and modules: round, math, random, etc.
- Expressions; unlimited integer precision; bitwise operations; hex, octal, and binary formats
- Third-party extensions: vectors, libraries, visualization, plotting, etc.

## Numeric Literals

| Literals | interpretation |
|----------|----------------|
| 1234, -24, 0, 99999999999999 | Integers (unlimited size) |
| 1.23, 1., 3.14e-10, 4E210, 4.0e+210 | Floating-point numbers |
| 0o177, 0x9ff, 0b101010 | Octal, hex, and binary literals |
| 3+4j, 3.0+4.0j, 3J | Complex number literals |
| set('spam'), {1, 2, 3, 4} | Sets: construction forms |
| Decimal('1.0'), Fraction(1, 3) | Decimal and fraction extension types |
| bool(X), True, False | Boolean type and constants |

> ### Complex numbers
>
> Python complex literals are written as ***realpart + imaginarypart***, where the imaginarypart is terminated with a **j** or **J**. The ***realpart*** is technically optional, so the ***imaginarypart*** may appear on its own.Internally, complex numbers are implemented as pairs of floating-point numbers, but all numeric operations perform complex math when applied to complex numbers. 
>
> Complex numbers may also be created with the **`complex(real, imag)`** built-in call.

## Build-in Numeric Tools

#### Python provides a set of tools for processing number objects:

*Expression operators*: `+`, `-`, `*`, `/`, `>>`, `**`, `&`, __etc.__

*Build-in mathematical functions*: `pow`, `abs`, `round`, `int`, `hex`, `bin`, __etc.__

*Utility modules*: `random`, `math`, __etc.__


## Python expression operators and precedence

| Operators | Description |
|-----------|-------------|
| `yield x` | Generator function send protocol |
| `lambda args: expression` | Anonymous function generation |
| `x if y else z` | Ternary selection (x is evaluated only if y is true) |
| `x or y` | Logical OR (y is evaluated only if x is false) |
| `x and y` | Logical AND (y is evaluated only if x is true) |
| `not x` | Logical negation |
| `x in y, x not in y` | Membership (iterables, sets) |
| `x is y, x is not y` | Object identity tests |
| `x < y`, `x <= y`, `x > y`, `x >= y` | Magnitude comparison, set subset and superset; |
| `x == y`, `x != y` | Value equality operators |
| `x \| y` | Bitwise OR, set union |
| `x ^ y` | Bitwise XOR, set symmetric difference |
| `x & y` | Bitwise AND, set intersection |
| `x << y`, `x >> y` | Shift x left or right by y bits |
| `x + y` | Addition, concatenation; |
| `x – y` | Subtraction, set difference |
| `x * y` | Multiplication, repetition; |
| `x % y` | Remainder, format; |
| `x / y`, `x // y` | Division: true and floor |
| `−x`, `+x` | Negation, identity |
| `˜x` | Bitwise NOT (inversion) |
| `x ** y` | Power (exponentiation) |
| `x[i]` | Indexing (sequence, mapping, others) |
| `x[i:j:k]` | Slicing |
| `x(...)` | Call (function, method, class, other callable) |
| `x.attr` | Attribute reference |
| `(...)` | Tuple, expression, generator expression |
| `[...]` | List, list comprehension |
| `{...}` | Dictionary, set, set and dictionary comprehensions |


> Operators lower in the table have higher precedence, and so blind more tighly in mixed expression.
>
> Operators in the same row in the table generally group from left to right when combined (except for exponentiation, which groups right to left, and comparisons, which chain left to right).


### Mixed operators follow operator precedence

When you write an expression with more than one operator, Python groups it's parts according to what are called *Precedence rules*, and this grouping determines the order in which the expression's parts are computed.

## Comparisons 

Python allows us to *chain* mutiple comparisons together to perform range tests. Chained comparisons are a sort of shorthand for boolean expressions.

> For instance, the expression **`(A < B < C)`** tests whether **`B`** is between **`A`** and **`C`**.  
It's equivalent to the boolean test **`(A < B and B < C)`**.


```python
X = 2
Y = 4
Z = 6

print(X < Y < Z) #Output: True

print(1 == 2 < 3) #Output: False
#Not same as: False < 3 (Which means 0 < 3, which is true)
```

## Division

- ***True division***: In Python 3.X, it performs *true* division, always keeping remainders in floating-point results, regardless of types.

```python
X = 5
Y = 2

print(X / Y) #Output: 2.5
```

- ***Floor division***: The // operator is informally called *trucating* division, but it's more accurate to refer to it as *floor* division. It truncates fractional remainders down to their floor, reguardless of types. Its result type depends on the types of its operands.

```python
X = 5
Y = 2

print(X // Y) #Output: 2
```

### Floor vs Truncation

The *floor* division truncates the result down to its floor, which means the closest whole number below the true result. The net effect is to round down, not strictly truncate, and this matters for negetives.

```python
import math

# floor() : Closest number below the true value

print(math.floor(2.5)) # Output: 2

print(math.floor(-2.5)) # Output: -3

# trunc() : Truncate fractional part (towards zero)

print(math.trunc(2.5)) # Output: 2

print(math.trunc(-2.5)) # Output: -2
```

> ### If you face trouble to understand the above example the table below will help
>
>| `-3` | `-2.5` | `-2` | -1.5 | -1 | -0.5 | `0` | 0.5 | 1 | 1.5 | `2` | `2.5` | 3 |  
>|------|--------|------|------|----|------|-----|-----|---|-----|-----|-------|---|


### Why does trucation matter

```python
# True division
print(5 / 2) # Output: 2.5
print(5 / 2.0) # Output: 2.5
print(5 / -2.0) # Output: -2.5
print(5 / -2) # Output: -2.5

# Floor division
print(5 // 2) # Output: 2
print(5 // 2.0) # Output: 2.0
print(5 // -2.0) # Output: -3.0
print(5 // -2) # Output: -3
```

## Hex, Octal, Binary: Literals and Conversions

Python integers can be coded in hexadecimal, octal and binary notation. Keep in mind that these lierals are simply an alternative syntax for specifying the value of an integer object.  

>For example, the following literals produce normal integers with the specified values in all three bases. In memory, an integer's value is the same, regardless of the base we use to specify it.

```python
# Octal literals: base 8; digits: 0-7

print(0o1) # Output: 1
print(0o20) # Output: 16
print(0o377) # Output: 255

# Hex literals: base 16; digits: 0-9 / A-F

print(0x1) # Output: 1
print(0x10) # Output: 16
print(0xFF) # Output: 255

#Binary literals: base 2; digits: 0-1

print(0b1) # Output: 1
print(0b10000) # Output: 16
print(0b11111111) # Output: 255
```

Python prints integer values in decimal (base 10) by default but provides build-in functions that allow you to convert integers to other bases digit strings.

```python
# Decimal to Octal
print(oct(20)) # Output: '0o24'

# Decimal to Hex
print(hex(15)) # Output: '0xF'

# Decimal to Binary
print(bin(32)) # Output: '0b100000'
```

The above build-in functions converts decimal to octal, hex and decimal depending on what function you use, but all these function returns the converted result into string.  

To go the other way, the build-in funcion `int()` converts string of digits to integers, and an optional second argument lets you specify the numeric base.

```python
print(int('100', 8)) # Output: 64
print(int('40', 16)) # Output: 64
print(int('1000000', 2)) # Output: 64

# Literal forms are supported too

print(int('0x40', 16)) # Output: 64
print(int('0b1000000', 2)) # Output: 64
```

The `eval()` function, treats strings as though they were Python code. Therefore, it has similer effect, but usually runs more *slowly*.

```python
print(eval('0xFF')) # Output: 255
```

Finally, you can also convert integers to base-specific strings with *string formating* method calls and expressions, which return just digits, not Python literal strings.

```python
conversion = '{0:o}, {1:x}, {2:b}'.format(64, 64, 64)

print(conversion) # Output: 100, 40, 1000000

conversion = '%o, %x, %x, %X' % (64, 64, 255, 255)

print(conversion) # Output: 100, 40, ff, FF
```

## Bitwise Operations

Besides the normal numeric operations (addition, subtraction, and so on), Python supports most of the numeric expressions available in the C language. This includes operators that treat integers as strings of *binary bits*.

Here are some of Python's bitwise expression operators at work performing bitwise shitf and boolean operations on integers:

```python
# Left shit
x = 1 # Decimal 1 is 0001 in bits
left_shifted_x = x << 2 # Shift left 2 bits i.e., 0100
print(left_shifted_x) # Output: 4

# Bitwise OR
bitwise_or = x | 2 # Bitwise OR: 0001 | 0010 = 0011
print(bitwise_or) # Output: 3

# Bitwise AND
bitwise_and = x & 1 # Bitwise AND: 0001 & 0001 = 0001
print(bitwise_and) # Output: 1

# Bitwise XOR
x = 0xFF
print(bin(x)) # Output: '0b11111111'

bitwise_xor = x ^ 0b10101010 # Bitwise XOR: 11111111 ^ 10101010 = 1010101
print(bitwise_xor) # Output: 85
print(bin(bitwise_xor)) # Output: '0b1010101'
```

>### Finding bit length
>
>Python provides a build-in method called `bit_length()`, which allows you to query the number of bits required to represent a number's value in binary. You can often achieve the same effect by *subtracting* `2` from from the length of the **bin** string using the `len()` build-in function, though it may be less effecient.
>
>```python
>x = 32
>print(x.bit_length()) # Output: 6
>print(len(bin(x)) - 2) # Output: 6
>
>print((256).bit_length()) # Output: 9
>```

## Other Build-in Numeric Tools

In addition to its core object types, Python also provides both built-in *functions* and standard library *modules* for numeric processing. The `pow()` and `abs()` built-in functions, for instance, compute powers and absolute values,respectively. Here are some examples of the built-in **math** module:

```python
import math

# Common constants
print(math.pi) # Output: 3.141592653589793
print(math.e) # Output: 2.718281828459045

# Sine, tangent, cosine
print(math.sin(2 * math.pi / 180)) # Output: 0.03489949670250097

# Square root
print(math.sqrt(144)) # Output: 12.0

# Exponentiation (power)
print(pow(2, 3)) # Output: 8
print(2 ** 3) # Output: 8
print(2.0 ** 3.0) # Output: 8.0

# Absolute value
print(abs(-42.0)) # Output: 42.0

# Summation
print(sum(1, 2, 3, 4)) # Output: 10

# Minimun and Maximum
print(min(3, 2, 1, 4)) # Output: 1
print(max(3, 2, 1, 4)) # Output: 4

# Round
print(round(2.567)) # Output: 3
print(round(2.567, 2)) # Output: 2.57

```

## Other Numeric Types

So far in this chapter, we’ve been using Python’s core numeric types—integer, floating point, and complex. These will suffice for most of the number crunching that most programmers will ever need to do. Python comes with a handful of more exotic numeric types, though, that merit a brief look here.

### Decimal Type

Python 2.4 introduced a new core numeric type: the decimal object, formally known as **Decimal**. Syntactically, you create decimals by calling a function within an imported module, rather than running a literal expression. Functionally, decimals are like *floating-point* numbers, but they have a fixed number of decimal points. Hence, decimals are *fixed-precision* floating-point values.  

For example, with decimals, we can have a floating-point value that always retains just two decimal digits. Because of the limited space used to store the floating-point values, floating-point math is less than exact. Take a look at the below example:

```python
print(0.1 + 0.1 + 0.1 - 0.3) # Output: 5.551115123125783e-17

```

As you can see, the above example should yield zero. but it does not. The result is close to zero, but there are not enough bits to be precise here.  

However, with decimals, the result can be dead-on:

```python
from decimal import Decimal

print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')) # Output: 0.0

```

As shown here, we can make decimal objects by calling the `Decimal` constructor function in the `decimal` module and passing in strings that have the desired number of decimal digits for the resulting object.

### Fraction Type

Python 2.6 and 3.0 debuted a new numeric type, Fraction, which implements a rational number object. It essentially keeps both a numerator and a denominator explicitly, so as to avoid some of the inaccuracies and limitations of floating-point math.  

```python
from fractions import Fraction

x = Fraction(1, 3) # Numerator, denominator
y = Fraction(4, 6) # Simplified to (2, 3) by gcd

print(y) # Output: 2/3
```

Once created, Fractions can be used in mathematical expressions as usual:

```python
print(x + y) # Output: 1

print(x - y) # Output: -1/3

print(x * y) # Output: 2/9
```

Fraction objects can also be created from floating-point number strings.

```python
print(Fraction('.25')) # Output: 1/4
```