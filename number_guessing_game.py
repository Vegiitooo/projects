import random
import math

print("====================")
print("Number Guessing Game")
print("====================")
print("\n\n")
print("Enter the range of the two numbers-")

while True:
    try:
        x = int(input("From: "))
        break
    except:
        print("Please enter a valid number.")

while True:
    try:
        y = int(input("To: "))
        break
    except:
        print("Please enter a valid number.")
if x>y:
    rand = random.randint(y,x)
    print("Selected range for the numbers: " + str(y) + " to " + str(x))
    maxtries=math.log(x-y-1,2)
else:
    rand = random.randint(x,y)
    print("Selected range for the numbers: " + str(x) + " to " + str(y))
    maxtries=math.log(y-x-1,2)

print(f"You have {round(maxtries)} tries to guess the number.")
count=0

while count<maxtries:
    count+=1
    print("\n")
    try:
        check = input("Guess the number (q to quit): ")
        if check=="q" or check=="quit":
            print("Quitting...")
            break
        check=int(check)

        if check>rand:
            print("Oops! You guessed too high. Try again.")
        elif check<rand:
            print("Oops! You guessed too low. Try again.")
        elif check==rand:
            print("Tada!! You guessed the number. It was " + str(rand) + ".")
            print("Total Tries:", count)

            break
    except:
        print("You didn't enter a valid number. Please try again.")
        continue
    if count>=maxtries:
        print("\n")
        print("You've reached the maximum number of guessing limit. The answer was " + str(rand) + ". Better luck next time.")
        break
    print("Tries left:", round(maxtries-count))
