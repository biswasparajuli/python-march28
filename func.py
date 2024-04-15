def test():
    for i in range(2):
        print(i)
    print("hello World")


test()


def even_number():
    for i in range(2, 10, 2):
        print(i)


even_number()


# Positional Arguments
def print_data(a, n):
    print(a, n)


a = input("Enter Your First Name: ")
n = input("Enter Your Last Name: ")
print_data(a, n)
print("_____________________________")


# Default Arguments
def take_files(n):
    return n
    print("number of file", n)


a = take_files(5)
print(a)


def list_data(a):
        print("list", a)


a = ["Apple", "Ball", 1, 2]
list_data(a)
