from clear import clear

logo = '''
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
'''

print(logo)
print("Welcome to Treasure Island! \n")
print("Your mission is to find the treasure. \n")

proceed = True

while proceed:
    left_right = input('Would you like to go left or right?: \n'.lower())
    if left_right == "left":
        clear()
        print("The road ahead is clear, until you reach a river.. \n")
        swim_wait = input("Would you like to Swim or wait? \n".lower())
        if swim_wait == "swim":
            clear()
            print("You were attacked by trout and died. Game over.")
            proceed = False
        elif swim_wait == "wait":
            clear()
            print("While waiting, you find 3 different doors.. \n")
            which_door = input("Which door will you choose, Red, Blue or Yellow? \n".lower())
            if which_door == "red":
                clear()
                print("Ouch, you were burned by fire. Game over.")
                proceed = False
            elif which_door == "blue":
                clear()
                print("Oof, you were eaten by beasts. Game over.")
                proceed = False
            elif which_door == "yellow":
                print(logo)
                print("You found the treasure! Congratulations!!")
                proceed = False
    elif left_right == "right":
        clear()
        print("Fall into a hole. Game over.")
        proceed = False







