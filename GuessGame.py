from random import randint
f=5
count=0
for i in range(f) :
    n= int(input("Enter any number between 1 to 100 :"))
    randomNum = randint(1,100)
    if n == randomNum:
        print("Congratulation you guess is correct")
        print("\n")
        count = count+1
    else:
        print("You have lost")
        print(f"Random Number is {randomNum}")
        print("\n")
print("Your Limit is over")
print(f"You Successfully Guess {count} times")