#This is a program for a faulty calculator which will print correct ans for any other basic calculations
#except for these few::::
# 59+9=77 
# 45*3=555
# 56/6=4

num1= int(input("Enter First Number:\t"))
num2= int(input("Enter Second Number:\t"))
opr=input("select operator \t+ \t- \t* \t/\n Your Operator is:\t")

if (opr== "+"):
    if (num1==59 and num2==9): #or (num1==9 and num2==59):
        print("ans:\t 77")
    else:
        num3 = num1 + num2
        print("ans:\t" ,num3)

elif (opr== "-"):
    num3 = num1 - num2
    print(num3)

elif (opr== "*"):
    if (num1==45 and num2==3): #or (num1==3 and num2==45):
        print("ans:\t 555")
    else:
        num3 = num1 * num2
        print("ans:\t" ,num3)

elif (opr== "/"):
    if (num1==56 and num2==6): #or (num1==6 and num2==56):
        print("ans:\t 4")
    else:
        num3 = num1 / num2
        print("ans:\t" ,num3)
else: 
    print("check input")
