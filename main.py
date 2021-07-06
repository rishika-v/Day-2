# < -less than, <=
# > - greater than, >=
# == - equal to
# != - not equal to

# and- both statements have to work
# or- either one statement has to work
# not - opposite of statement

#boolean

import random

ComputerNumber = random.randint(0,10)

maxguesses = 3
Win = False
Play = True

while Play == True:

  while maxguesses > 0:
    num = int(input("Enter a number (0-10): "))
    if num < ComputerNumber:
      print("Your guess is lesser than the number")
      maxguesses = maxguesses -1
      print(str(maxguesses) + " guesses left")
    elif num > ComputerNumber:
      print("Your guess is greater than the number")
      maxguesses = maxguesses -1
      print(str(maxguesses) + " guesses left")
    else:
      print("You got it!")
      Win = True
      maxguesses = 0



  if Win == True:
      print("Congratulations!")
  else:
      print("No more tries")
      print ("The number was: " + str(ComputerNumber))

  answer = input("Do you want to play again? Y/N ")
  if answer.upper() == "N":
      print("Game Over")
      Play = False
  else:
      Win = False
      maxguesses = 5