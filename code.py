import random
from random import randint

max_guesses = 4
number = random.randint(1, 19) # Change the numbers here if you wish to increase/decrease the possible numbers.

welcome = print("Welcome to the random number generator Game!")

for x in range(1, max_guesses + 1):
    try:
        user_guess = int(input(f"Attempt #{x}! Take a wild guess at the number: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        continue
    if user_guess == number:
        print("Congrats, you got it correct!")
        if x == 2:
            print(f"You got it correct on the {x}ND guess!")
        elif x == 1:
            print(f"You got it correct on the {x}ST guess!")
        elif x == 3:
            print(f"You got it correct on the {x}RD guess!")
        else:
            print(f"You got it correct on the {x}TH guess")
        break
    elif user_guess < number:   
        print("Too low, try again!")
    else: 
        print("Too high, try again") 
      # You can remove this line as well as the one above and simply replace it with "elif:...print("wrong, try again!") if you think "too low/too high" gives it away

    if x == max_guesses:
        print("Womp, womp, womp... You ran out of guesses!")
