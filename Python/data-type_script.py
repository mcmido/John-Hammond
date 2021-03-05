#!/usr/bin/env python
DataType = input("Input Smth To check it\'s type: ")
# Ain't working due to the fact that input takes str by default
# well see if i can fix it in the future
v = type (DataType)
print(v)
print ("Your Data is: " + str(v) )
