a=[]
for i in range(1,5):
    n = int(input("Enter the number: "))
    a.append(n)
for i in range(len(a)):
    for j in range(1,11):
        b = a[i]
        print(f'{b} X {j} = {b * j}')