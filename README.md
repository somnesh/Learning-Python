# Introduction to Python

Python is a general-purpose programming language that is often applied in scripting roles. It is commonly
defined as an ***object-oriented scripting language*** - a definition that blends support for OOP with an overall
orientation toward scripting roles. 

Python is probably better known as a ***general-perpose programming language*** that blends procedural functional, and object-oriented paradigms - a statement that captures the richness and scope of today's Python.

## Introducing the Python Interpreter

An interpreter is a kind of program that executes other programs. When you write a Python program, the Python interpreter reads your program and carries out the instructions it contains. In effect the interpreter is a layer of software logic between your code and the computer hardware on your machine.

When the Python package is installed on your machine, it generates a number of components - minimally, an interpreter and a support library. 

## Program Execution (Python's View)

When you instruct Python to run your script, there are a few steps that Python carries out before your code actually starts crunching away. Specifically, it's first compiled to something called "Byte-code" and then routed to something called a "virtual machine".

### <ins>Byte code compilation</ins>

Internally, and almost completely hidden from you, when you execute a program Python first compiles your *source code* into a format known as *byte code*. Compilation is simply a translation step, and byte code is lower level, platform-independent representation of your source code. Roughly, Python translates each of your source statements into a group of byte code instructions by decomposing them into individual steps. This byte code translation is performed to speed execution - byte code can be run much more quickly than the original source code statements in your text file.

You'll notice that the prior paragraph said that this is *almost* completely hidden from you. If the Python process has write access on your machine, it will store the byte code of your programs in files that ends with a *.pyc* extension (".pyc" means compiled ".py" source).

In 3.2 and later, Python saves it's *.pyc* byte code files in a sub-directory named \__*Pycache*__ located in the directory where your source files reside, and in files whose names identify by the Python version that crated them (e.g., *script.cpython-33.pyc*). The \__*Pycache*__ sub-directory helps to avoid clutter, and the naming convention for byte code files prevents different Python versions installed on the same computer from overwriting each other's saved byte codes.

Python saves byte code like this is a startup speed optimization. The next time you run your program, Python will load the *.pyc* files and skip the compilation step, as long as you haven't changed your source code since the byte code since the byte code was last saved, and aren't running with a different Python than the one that created the byte code. It works like this:

- ***Source changes***: Python automatically checks the last-modified timestamps of source code and byte code files to know when it must recompile - if you edit and resave your source code, byte code is automatically re-created the next time your program is run.

- ***Python versions***: Imports also check to see if the file must be recompiled because it was created by a different Python version, using either a "magic" version number in the byte code file itself in 3.2 and earlier, or the information present in byte code filenames in 3.2 and later.

If Python cannot write the byte code files to your machine, your program still works - the byte code is generated in memory and simply discarded on program exit.

> Finally, keep in mind that byte code is saved in files only for files that are *imported*, not for the top-level files of a program that are only run as scripts.

### The Python Virtual Machine (PVM)

Once, your program has been compiled to byte code (or the byte code has been loaded from existing *.pyc* files), it is shipped off for execution to something generally known as the Python Virtual Machine.

The PVM sounds more impressive than it is, it is not a separate program, and it need not to be installed by itself. In fact, the PVM is just a big code loop that iterates through your byte code instructions, one by one, to carry out their operations. The PVM is the runtime engine of Python, it is always present as part of the Python system, and it's the component that truly runs your scripts. Technically, it's the just the last step of what is called the "Python interpreter".