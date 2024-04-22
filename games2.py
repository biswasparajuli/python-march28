import random

a = """

1 = rock
0 = scissor
2 = paper

"""

print(a)

random_number = random.randint(0, 2)
n = int(input("enter a number "))
print(random_number)

if n == random_number:
    print("its tie bro ")

if (
    (random_number == 1 and n == 2)
    or (random_number == 0 and n == 1)
    or (random_number == 2 and n == 0)
):
    print("you won bro!!")
else:
    print("Sorry bro")
