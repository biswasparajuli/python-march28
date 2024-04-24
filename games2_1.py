import random

a = """

1 = rock
0 = scissor
2 = paper

"""

print(a)

random_number = random.randint(0, 2)
print(random_number)
n = int(input("enter a number "))

while random_number != n and n < 3:
    if (
        (random_number == 1 and n == 2)
        or (random_number == 0 and n == 1)
        or (random_number == 2 and n == 0)
    ):
        print("you won bro!!")
        break
    else:
        print("You Lose")
        n = int(input("Again enter a number: "))
if random_number == n:
    print("It is tie bro")
elif n > 3:
    print(f"You have entered invalid number i.e. {n}. Please enter among 0, 1 or 2 ")
