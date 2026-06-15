from random import randint
guessNum =int(input("Enter your guess between 1 to 100: "))
randomNum = randint(1,101)

if guessNum == randomNum :
    print("Congretulations you have won the game!!")
else:
    print("You have lost the game")
    print(f"Random Number was: {randomNum}")