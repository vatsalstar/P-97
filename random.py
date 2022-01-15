import random
number=random.randint(1,9)
chances=0
while chances<2:
    guess=int(input("aray bhai number guess kar"))
    if(guess==number):
        print("YOU WON")
        break
    elif(guess<number):
        print("your guess was very low TRY AGAIN!")

    else:
        print("Your Guess Was Too High")

    chances=chances+1

if(chances>2):
    print("YOU LOSE!!!!")
    print("The Number Was"+number)
    



