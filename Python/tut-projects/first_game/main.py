#!/usr/bin/env python3 	
print("Welcome To my first game!")



age = int(input("Type Your Age: "))

health = 10



if age >= 16:
	print("Your old enough to play the game!")

	wants_to_play = input("Do You Want To Play? (Yes,No)!").lower()

	if wants_to_play == "yes":
		print("Lets Play!")
		print("you are starting with", health, "health")

		left_or_right = input("First Choice... Left or right (Left or Right)").lower()
		if left_or_right == "left":

			ans = input("Nice, you followed the path and reached a lake... \nDo you swim across or go around (across/around)").lower()

			if ans == "around":
				print("You Went around and reached the other side of the lake")

			elif ans == "across":
				print("you managed to get across, but were bit by a fish and lost 5 health")
				health -= 5

			ans = input("you notice a house and a river which do you go to (river/house)? ")

			if ans == "house":

				print("you go to the house and are greted by the owner... he dosn't like you and you lose 5 health")
				health -= 5

				if health <= 0:
					print("You now have 0 health and you lose the game...")
				else:
					print("You have survived..... YOU WIN!!!")
			else:
				print("you fell down the river and lost...")
		else:
			print("you fell donw and lost....")
	else:
		print("Cya...")
else:
	print("blah")

