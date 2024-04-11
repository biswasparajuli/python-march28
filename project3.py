# Type 1 as you entered number your table will be printed
a=[]
for i in range(1,5):
    n = int(input(f'Enter the {i} number:'))
    a.append(n)
    for i in range(len(a)):
        print(f'Multiplication table of {n}')
        for j in range(1,11):
            b = a[i]
            print(f'{b} X {j} = {b * j}')

# Type 2 as first you entered all number then your table will be printed once
a=[]
for i in range(1,5):
    n = int(input(f'Enter the {i} number:'))
    a.append(n)
for i in range(len(a)):
    print(f'Multiplication table of {n}')
    for j in range(1,11):
        b = a[i]
        print(f'{b} X {j} = {b * j}')