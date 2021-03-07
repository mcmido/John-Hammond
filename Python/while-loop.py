#!/usr/bin/env python3

# While Loop
print("Welcome to my game!")

choice = ""
while choice != "quit":
	choice = input("What would you like to do?\n> ")
	print("Going through the loop")
	print("your choice was: ",choice)

print("we're done! something_true is now", choice)
