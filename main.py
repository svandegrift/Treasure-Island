#!/usr/bin/env python3
# Day 3 - Treasure Island - Steven Vandegrift 2021
print('''
*******************************************************************************
		  |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
		  |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
		  |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
decision1 = input("You are at a cross road. Where do you want to go? Type 'left' or 'right'\n")
if decision1.lower() == "left":
	decision2 = input("You walk down the road until you reach the beach. \nThere you see there is a fishermen offering rides in his boat but he is currently out at sea. \nYou can see the island within view. \nDo you wait for the fishermen to come back or swim towards the island yourself? \nType 'swim' or 'wait'\n")
	if decision2.lower() == "swim":
		print("You decided that swimming miles of water was a good idea. You don't even make it to the mile mark before a bunch of trout decide you are their next meal. Game Over")
	elif decision2.lower() == "wait":
		decision3 = input("You wait only 30 minutes for the fishermen to return. \nYou get on the boat and make it to treasure island. \nSurprisingly it looks like a 5 star hotel is on it. \nYou go into the hotel and come across 3 doors. \nThe doors are red, yellow, and blue. Which door do you choose? \nType 'red' 'yellow' or 'blue'\n")
		if decision3.lower() == "red":
			print("This room is full of TNT! By opening the door you trip the sensor that activates it all instantly!!! \nU insta dead. Game Over.")
		elif decision3.lower() == "yellow":
			print("You open the door to find all of the gold! You take it by the hand full and run back to the boat. You're rich! YOU WIN!")
		elif decision3.lower() == "blue":
			print("THIS ROOM IS FULL OF HUNGRY WOLVES! WHO WOULD DO SUCH A THING?!?!? \nYou try to escape but cannot outrun them! U super dead... Game Over")
		else:
			print("You are so overwhelmed with 3 decision you device it is best to do nothing and have fate decide your destiny. \nAfter a few hours of standing there another treasure hunter comes in, looks and the 3 doors and instantly decides to open the red door unlike you. \nToo bad the room is filled with explosives rigged to blow the moment the door was opened. \nYou both be insta dead. Game Over.")
	else:
		print("You sit there. You do absolutely nothing but watch as the waves hit the sand. \nThat is until a hurricane approaches and sweeps you into the air. \nYou fly all the way back past where you started... Game Over.")
elif decision1.lower() == "right":
	print("You walk right of days, only to realize it takes you to the desert... No where near the water... It's Game Over bro")
else:
	print("You failed to make one of the two decisions. You stand there. \nHours go by. Weeks go by. Your body and mind start to deteriorate as hunger begins to set in. \nYou eventually close your eyes only to wake in the void that is the afterlife..... \nGame Over.")

	