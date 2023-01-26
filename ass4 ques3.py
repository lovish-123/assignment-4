#multiplication game program for kids
import random
i = 0
temp = 0
while i<10 :
    a=random.randrange(0,10)
    b=random.randrange(0,10)
    print("question",i+1," :",a,"*",b,"=")
    k = int(input())
    i = i+1
    if k == a*b :
        print("correct")
        temp+=1
    else:
        print("wrong")
if temp<=5:
    print("sorry only ",temp, "correct ")
else:
    print("congratulations",temp,"correct")


