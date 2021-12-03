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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
decision1 = input("You are at a cross road. Where do you want to go? Type 'left' or 'right'\n")
if decision1.lower() == "left":
	decision2 = input("You walk down the road until you reach the beach. There you see there is a fishermen offering ride in his boat but he is currently out at sea. You can see the island within view. Do you wait for the fishermen to come back or swim towards the island yourself? Type 'swim' or 'wait'\n")
	if decision2.lower() == "swim":
		print("You decided that swimming miles of water was a good idea. You don't even make it to the mile mark before a bunch of trout decide you are their next meal. Game Over")
	elif decision2.lower() == "wait":
		decision3 = input("You wait only 30 minutes for the fishermen to return. You get on the boat and make it to treasure island. Surprisingly it looks like a 5 star hotel is on it. You go into the hotel and come across 3 doors. The doors are red, yellow, and blue. Which door do you choose? Type 'red' 'yellow' or 'blue'")
	else:
		print("You sit there. You do absolutely nothing but watch as the waves hit the sand. That is until a hurricane approaches and sweeps you into the air. You fly all the way back past where you started... into a hole... Game Over.")
elif decision1.lower() == "right":
	print("You walk left of days, only to realize it takes you to the desert... No where near the water... It's Game Over bro")
else:
	print("You failed to make one of the two decisions. You stand there. Hours go by. Weeks go by. Your body and mind start to deteriorate as hunger begins to set in. You eventually close your eyes only to wake in the void that is the afterlife..... Game Over.")

	