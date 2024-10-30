import random

randnum = random.randint(1,20)
# print(randnum)
guesses = 0
userguess = None

print("Please enter the number between 1 to 20")
while(userguess != randnum ):
    userguess =  int(input("Please enter you guess \n"))
    guesses+=1
    if (userguess==randnum):
        print("******Congratulation You WON ******")
    else:
        if (userguess<randnum ):
            print("you guessed wrong, please enter the larger number")
        else:
            print("you guessed wrong, please enter the smaller number")



with open("game.txt", "r") as f:
        hiscore = int(f.read())
if hiscore >  guesses:
     with open("game.txt", "w") as f:
          f.write(str(guesses))
     print(f"you broke the record in {guesses} guesses ")
else:
     print(f"you guessed the number in {guesses} guesses ")




