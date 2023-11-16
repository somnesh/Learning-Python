'''
File objects are Python code`s main interface to external files on your computer.

There is no specific literal syntax for creating a file, Rather to create a file object you call the 
build-in open() function, passinga an external filename and an optional processing mode as strings.

'''

F = open("test.txt","w")

print(F.write("Hello\n")) #output : 6 (Because it returns the number of items written)
F.write("World")

F.close() 

'''
To read back what you just wrote, reopen the file in 'r' processing mode, for reading text inputs.

A file's contents are always a string in your script, regardless of the type of data the file contains.

'''

F = open("test.txt") #'r'(read) is the default processing mode
text = F.read()

print(text)

#File content is always a string so, we can manipulate it using build-in-functions for strings.
print(text.split())

F.close()

#Files provide an iterator that automatically reads line by line in for loops or other contexts
for line in open("test.txt"):
    print(line)

F.close()