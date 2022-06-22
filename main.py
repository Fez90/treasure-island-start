# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
choice1 = input("where do you wanna to go? type 'left' or 'right'.").lower()
if choice1 == "left":
  choice2 = input("do you wanna 'swim' or 'wait'?").lower()
  if choice2 == "wait":
    choice3 = input("which door do you choose? red, blue and yellow?").lower()
    if choice3 == "red":
     print("room of fire.game over")
    elif choice3 == "yellow":
      print("you win!")
    elif choice3 == "blue":
      print("attacked by beasts.game over")
    else:
      print("game over")
  else:
      print("you got attacked by trout. game over")
else:
    print("fall from the cliff. game over")











# l = input("Where are you going? left or right?") 
# if l == "left":
#   if input("swim or wait?") == "wait":
#     if input("Which door?") == "blue":
#       if input("Which door?") == "red":
#        if input("Which door?") == "yellow":
#           print("You win!")
#        else:
#           print("game over")
#       else:
#        print("burned by fire. game over")
#     else:
#       print("attacked by beasts.game over")
#   else:
#     print("attacked by trout. game over")
# else:
#   print("Fall into the hole. Game over.")
