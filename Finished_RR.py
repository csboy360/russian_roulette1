# imports and variables
import random
import sys
trig = "*PULLS TRIGGER*"
compbang = "*BANG!* The computer is dead. YOU SURVIVED!!"
compsafe = "The computer is SAFE! The gun was passed"
userbang = "*BANG!* You are dead. The computer survived. GAME OVER"
usersafe = "Whew. Your SAFE... You passed the gun"


# when user input is false this loop goes into the next turn
def falsefun():
    while userinput > intodds:
        failint = float(input("Please eneter a number "  + strodds + " or less"))
        if failint <= intodds:
            break
    input(trig)
    if failint == ranint:
            print(userbang)
            sys.exit()
    else:
            input(usersafe)

# when user input is true this loop goes into the next turn
def truefun():
    input(trig)
    if userinput == ranint:
        print(userbang)
        sys.exit()
    else:
        input(usersafe)



# INTRO

print("Welcome to Russian Roulette. This is how it works. Just like the real-life roulette, there is 1 in the chamber. \n   Every turn a random number carries the bullet and your odds get"
      " worse. If your number matches, your dead. \n                              In this game you can either WIN, SURVIVE, OR DIE \n                                  (Press Enter) ")

# TURN 1 GAME STARTS

ranint = (random.randint(1 ,6))
strodds = str(6)
intodds = float(6)


userinput = float(input("Okay YOU'RE up. Type a number between 1 and 6"))

if userinput > 6:
    falsefun()
else:
    truefun()


# TURN 2 (computer)
ranint = (random.randint(1 ,5))
input("The computer entered a number between 1 and 5")

input(trig)
if ranint == 2:
    input(compbang)
    sys.exit()
else:
    input(compsafe)

# TURN 3
ranint = (random.randint(1 ,4))
userinput = float (input("Okay YOU'RE up. Type a number between 1 and 4"))
strodds = str(4)
intodds = float(4)

if userinput > 4:
    falsefun()
else:
    truefun()

# TURN 4 (computer)
ranint = (random.randint(1 ,3))
input("The computer entered a number between 1 and 3")

input(trig)
if ranint == 3:
    input(compbang)
    sys.exit()
else:
    input(compsafe)

# TURN 5
ranint = (random.randint(1 ,2))
userinput = float (input("Okay YOU'RE up. Type a number between 1 and 2"))
strodds = str(2)
intodds = float(2)

if userinput > 2:
    falsefun()
else:
    truefun()
# TURN 6
input("The computer AIMED the gun at you!")
input("You tried to wrestle him for THE GUN!")

input(trig)

ranint = (random.randint(1 ,3))
if ranint == 3:
    input("*BANG!* You are dead. The computer WON!!!")
    sys.exit()
else:
    input("*BANG!* WINNER WINNER! CHICKEN DINNER!! You put a bullet threw his head. Keep up the good work.")