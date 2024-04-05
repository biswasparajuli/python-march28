# Project about the interest after the divison secured
# Slab for the project 100-80 (Distinction), with 100-90 "Study Prasadi Academy" and 80-90 "Study St. Xavier" 
# 80-60 (First Division), with 80-70 "Study ABC Management" and 70-60 "Study BCD Management"
# 60-45 (second Division), run business
# 45-35 (Third Division), Foreign Employment 
# Below 35 (fail), Study Again
done = input("Enter Your Secured Marks")
marks=int(done)
if( marks <=100 and marks >=80 ):
    print ("You have Secured Distinction, Congratulation")
    if(marks <=100 and marks >=90):
        print("Study Prasadi Academy")
    else:
        print("Study St. Xavier")
elif( marks <80 and marks >=60 ):
    print ("You have secured First Divison")
    if(marks <=80 and marks >=70):
        print("Study ABC Management")
    else:
        print("Study BCD Management")
elif( marks <60 and marks >=45 ):
    print ("You have secured Second Division")
    print("Run Business")
elif( marks <45 and marks >=35 ):
    print ("You have secured Third Divison")
    print("Try Foreign Employment")
elif( marks <35 and marks >=0 ):
    print ("Sorry you are fail")
    print("Study Again")
else:
    print ("Invalid Number Range")
