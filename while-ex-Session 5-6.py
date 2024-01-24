import random
lives = 3

while lives > 0:
    print("you have", lives, "lives left")
    dice_roll = random.randint(1, 6)
    if dice_roll == 6:
        print("you win")
        break
    else:
        print("you rolled a", dice_roll, "try again")
        lives = lives - 1

if lives == 0:
    print("you lost all your lives, game over")
