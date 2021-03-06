#!/usr/bin/env python3

# Simple Structure
#if conditional_statment:
#	statment()

'''
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


# The first one to evaluate to True 'wins'

if 3!= 3:
	print('Strange...')
elif 8 == 8:
	print("First True elif Found....")
elif 8 > 4:
	print("second True elif found....")	

##################################################
# More complicated, but all the same rules apply

print("This happens befor the 'if' block")

'''

user_is_admin = True

# What conditionals allow you to do

if user_is_admin:
	print ("Access Granted.")
	command = input("How would you like to proceed??")

	command = command.lower()
	if command == "destroy datacores":
		print("Destroying All Datacores")

	elif command == "exit":
		print("You don't have the guts, do you?")
	else:
		print("Access Denied, no correct answer")

else:
	print("Access Denied.")

print("This Happens after the 'if' block.")