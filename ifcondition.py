# Syntax if (condition) : result {for true condition}
# Syntax if (condition) : result {for false condition} Else: result2 next
# Syntax if (condition) : result {for false condition} elif(condition2): result2 Else: result3 i.e. next
# nested Condition
# Syntax if (condition) : result if (condtion): result 
# we can even use our else in this nested if
if (2==2):
    print("True")
if (3==2):
    print("True")
else:
    print(False)
marks = 70
if (marks>80):
    print("Read Science")
elif (marks<80):
    print ("Read Management")
else:
    print ("Read Arts")
if (2==2 or 1==4):
    print("Condition True")
