# Valid way to define variable
color = "red"
Color = "green"
_color = "black"

# Invalid way to define variable
# 5test = "Yes"
# $test = 1
a,b = 3 , 2
print(a,b)
a = b = 1
print(a,b)
# Data Must be given by the user i.e. Dynamic
a = input("Enter a number")
print (a)
b = input("Enter 2nd Number")
print (b)
c = a + b
print (c)
# input always take into string i.e. a=1 b=2 then c=12
# we should type cast to change string into number
a = int(input("Enter a number"))
b = int(input("Enter 2nd number"))
c = a+b
result="This is result" + str(sum)
print (result)
print("result is", a + b, "Sudhan")
print (c)
print (a+b) # this fuction reduces c value
a = float(input("Enter a number"))
b = float(input("Enter 2nd number"))
print (a+b)