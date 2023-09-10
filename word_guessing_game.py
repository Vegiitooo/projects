import random


wordlist = ['apple', 'world', 'raiden', 'rainbow', 'cloud',
            'control', 'thunder', 'house', 'window']
word = random.choice(wordlist)
guesses = ''

turns=10

while turns>0:
    print("\n")
    remaining=0
    for char in word:
        if char in guesses:
            print(char, end=' ')
        else:
            print('_', end=' ')
            remaining+=1
        
    if remaining==0:
        print("\nYou win.")
        break
    print("\n")

    x = input("Guess the missing letter: ")
    if len(x)>1:
        if x=='quit':
            print("Exiting...")
            break
        else:
            print("Please enter a single letter to guess.")
            continue
    else:
        if x in guesses:
            print("You've already guessed that letter.")
        else:
            guesses+=x
    if x not in word:
        turns-=1
        print("Wrong guess.")
        print("Turns Left: " + str(turns))
    
    if turns==0:
        print("You've exceeded the maximum number of guesses.\nThe word was '" + word + "'. You lose.")
