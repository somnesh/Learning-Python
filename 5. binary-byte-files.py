'''
The difference between a text file and a binary file:

Text files represent content as normal strings and perform Unicode encoding and decoding automatically
when writing and reading data, 

while binary files represent content as a special bytes string and allow you to access file content unaltered.


Python's "struct" module can both create and unpack packed binary data, raw bytes that record values that are
not python objects and to be written to a file in binary mode.

'''
import struct

packed = struct.pack('>i4sh', 7, b'spam', 8)

'''
In the above code here, '>i4sh' is a format string and the values we are trying to pack into it.

Let's break down the format string:

(i) '>' : This indicates that the data should be packed in big-endian (Most significant byte first) order.
(ii) 'i' : This indicates a 4-byte or 32-bit integer.
(iii) '4s' : This indicates a 4-byte or 32-bit string.
(iv) 'h' : This indicates a 2-byte or 16-bit short integer.

The 'b' infront of 'spam' indicates it is an bytes literal not a sequence of Unicode characters.
'''

print(packed)


#Output: b'\x00\x00\x00\x07spam\x00\x08'

#Let's break down the output:

#First, each '\x' represents a hexadecimal escape sequence.

#'\x00\x00\x00\x07' corresponds to a 32-bit integer with the hexadecimal value '0x00000007', i.e. the number 7

#'spam' is the 4-byte string

#'\x00\x08' corresponds to a 16-bit short integer with a hexadecimal value '0x0008', which is the number 8


file = open('test.bin','wb') #'wb' : write binary
print(file.write(packed)) #output: 10 (10-bytes of data has been written)
file.close()

#Reading and Unpacking a binary data file

data = open('test.bin','rb').read() #'rb' : read binary
print(data)

print(struct.unpack('>i4sh', data)) #Unpacking into objects again