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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

first_choice = (input("You are standing at a crossroads and you can go either left or right.  Which way do you want to go? (left or right)\n")).lower()

if first_choice == "left":
  second_choice = (input("You walk for several miles on the road and come to a river, beyond which the road continues, you see a sign for a ferry but currently the ferry is not present.  Do you want to wait for the ferry to come back or attempt to swim accross the river? (swim or wait)\n")).lower()
  if second_choice == "wait":
    third_choice = (input("The ferry returns after some time and takes you across the river, where after a brief walk you find a large cathedral in a clearing.  You go inside.  Inside the vestibule you find three doors leading to different parts of the building.  One door is Red, The next Door is Yellow, the third Door is Blue.  You decide to explore further.  Which door do you choose? (red, yellow, or blue)\n")).lower()
    if third_choice == "red":
      print("You step inside a beautiful red room that glows mysteriously and smells of smoke.  As you are looking around the room suddenly bursts into flame and you are incinerated.  Game over.\n")
    elif third_choice == "yellow":
      print("You step into a beautiful golden room that glows and sparkles because it is full of gold and jewels.  You win!\n")
    elif third_choice == "blue":
     print("You step into a deep blue colored room that undulates stranglely.  Suddenly the floor collapses into an ocean full of sea creatures that eagerly devour you.  Game over.  Sea Creatures win!\n")
  else: 
    print("You try to bravely, or possibly foolishly, to cross the river by swimming.  Half-way across you feel something slimy against your leg briefly before you are pulled under.  You are drowned by some unknown horror, possibly just a slimy log.  Game Over.\n")
else:
  print("You turn to the right and start walking, suddenly you hear a rustle from behind a bush and zombies jump out an attack you, you are eaten. The zombies win. Game Over.\n")



