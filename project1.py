# Project about the Percentage
# Percentage Slab for the project 100-80 (Distinction), 80-60 (First Division), 60-45 (second Division), 45-35 (Third Division) and Below 35 (fail)
done = input("Enter You secured marks")
marks = int(done)
if marks <= 100 and marks >= 80:
    print("You have Secured Distinction, Congratulation")
elif marks < 80 and marks >= 60:
    print("You have secured First Divison")
elif marks < 60 and marks >= 45:
    print("You have secured Second Division")
elif marks < 45 and marks >= 35:
    print("You have secured Third Divison")
elif marks < 35 and marks >= 0:
    print("Sorry you are fail")
else:
    print("Invalid Number Range")
