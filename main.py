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
    num = input("Enter a number (0-10): ")
    if num < ComputerNumber:
      print("Your guess is lesser than the number")
    elif num > ComputerNumber:
      print("Your guess is greater than the number")
    else:
      print("You got it!")
      Win = True