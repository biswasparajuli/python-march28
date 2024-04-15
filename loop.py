# a = [1,2,3,4,5,6]
# for i in a:
# print (i)
# for j in "Sudan":
# print (j)
# for i in range(1,20,2): # Sntax range(starting value, ending value, range to jump)
#  print("Testing", i)
d = int(input("Enter the table of which you want "))
for i in range(1, 11, 1):
    # print(c, "X",i,"=",i*d)
    print(f"{d} X {i} = {i*d}")

# print data to desire data
ages = [19, 26, 29]
for i in range(0, len(ages)):
    print(ages[i])
    if ages[i] == 26:
        break
print("_________________________________")
for i in range(0, len(ages)):
    if ages[i] == 26:
        continue
    print(ages[i])
print("************************")
for i in range(1, 3):
    for j in range(1, 3):
        print(i, j)
