#!/usr/bin/env python3

# Simple Structure
#if conditional_statment:
#	statment()

	
# Example
command = "destroy datacores"
if command == "destroy datacores":
	print("Destroying all datacores")
# False v
command = "destroy datacores"
if 8 > 16:
	print("hello world")


# Optional Else
if command == "hello" and 8 > 1:
	pass
else:
	print("This executes only if the first condition is false")

# Optional Elif (Between Original conditional test and 'else' keyword)
command = input("How would you like to proceed?\n Chose Between: destroy datacores, shut down, permabork the frambulator.\n> ").lower()

if command == "destroy datacores":
	print("Destroying all datacores")

elif command == "shut down":
	print("Shutting The system down")

elif command == "permabork the frambulator":
	print("Are you sure? You will not be able to unbork this later..")

# None of the otheres evaluated to True
else:
	print("Command not understood.")	