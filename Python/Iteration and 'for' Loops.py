#!/usr/bin/env python3
# itteration > if you have a list of smth and you wanna do smth for each item in that list
 
programs_to_write = [
 	"slightly better bash script",
 	"web crawler",
 	"port scanner",
 	"web applications",
 	"cloud provisioning tool",
]

 # Basic Form - INDENTATION is Key!
for program_name in programs_to_write:
 	print("I'm going to writ a", program_name) # capitalize? 

print("\n ...We're done!")
print("but it's not all clean fun -- the loop variable --", program_name,"--still exists!")

grid=[]
for x in range(0,3):
	for y in range(0,3):
		grid.append([x,y])
		print("this is x",x,"this is y",y)

