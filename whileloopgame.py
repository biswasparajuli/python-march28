import random
n = random.randint(1,5)
print(n)
i=0
c=int(input(f'Enter a number: '))
while (c!=n):
    i=i+1
    print("Wrong")
    if (i==2):
        print("You have max tries")
        break
    c=int(input(f'Enter a number again: '))
if(n==c):    
    print(f'Welldone {c} is Correct quess and you quessed on {i+1} try')
