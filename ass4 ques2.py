a = int(input(" enter the year "))
if a%4==0 and a%100!=0:
    print("the year entered is a leap year ")
elif a%4==0 and a%100==0 and a%400==0:
    print("the year entered is a leap year")
else :
    print("the year entered is not a leap year")