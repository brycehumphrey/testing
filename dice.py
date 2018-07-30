import random

while True:

    # Asking how many dice they want to roll and storing that number
    try:
        numDice = int(input("How many dice do you want to roll? "))
    except ValueError:
        print("This is not a number. ")
        continue

    # Check for 0 dice, if 0 then start from the top of the main while loop
    if numDice == 0:
        print("You can't roll 0 dice.")
        continue

#s something something
# somasdfasdf jalsd j
    # Empty list for holding the sides of the dice
    sidedDice = []

    i = 1
    # Loop for asking how many sides of each dice.
    while (i <= numDice):
        hold = int(input("How many sides is the dice? "))
        if hold == 0:   # if input is 0 starts the whole loop over from the previous value of i
            print("You can't have a 0 sided dice. ")
            continue
        elif hold == 1:
            print("There are no 1 sided dice. ")
            continue
        else:
            sidedDice.append(hold)  # if number != 0 then place hold number in list
            i = i + 1   # add 1 to i

    # Loop for rolling the number of dice from 1 to their side
    for i in range(numDice):
        roll = random.randint(1,sidedDice[i])
        print("The %d sided die is %d." % (sidedDice[i], roll))

    # Asking user if they want to roll again
    goOn = input("Do you want to roll again? ")

    # If the user types yes then continue to the top of the loop, else end program
    if goOn == "yes" or goOn == "Yes" or goOn == "YES":
        continue
    else:
        print("Goodbye. ")
        # break
