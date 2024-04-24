import random

a = """

1 = rock
0 = scissor
2 = paper

"""

print(a)

game_start = "Y"
while game_start == "Y" or game_start == "y":
    random_number = random.randint(0, 2)
    # print(random_number)
    n = int(input("Welcome Player, Enter Your Choice "))
    if random_number == n:
        print("It is tie bro")
    elif n not in [0,1,2]:
        print(
            f"You have entered invalid number i.e. {n}. Please enter among 0, 1 or 2 "
        )
    elif (
        (random_number == 1 and n == 2)
        or (random_number == 0 and n == 1)
        or (random_number == 2 and n == 0)
    ):
        print("you won bro!!")
    else:
        print("You Lose")
    game_start = input(f"Do you want to play again: (Y/N) ")
