

def print_number():
    x = int(input("Enter an number for input output working ->"))
    print("Entered number--->",x)

def student_grade():
    marks = int(input("Enter marks to get the grades ->"))
    print("Your grade is")

    if(marks >= 90):
        print("Grade A")
    elif(marks >= 70):
        print("Grade B")
    elif(marks >= 50):
        print("Grade C")
    elif(marks >= 35):
        print("Grade D")
    else:
        print("Fail")


def whichWeekDay():
    day = int(input("Enter the day number ->"))

    match day:
        case 0:
            print("Sunday")

        case 1:
            print("Monday")

        case 2:
            print("Tuesday")

        case 3:
            print("Wednesday")

        case 4:
            print("Thursday")

        case 5:
            print("Friday")

        case 6:
            print("Staurday")

        case _:
            print("Invalid Day")

    

# print_number()
# student_grade()
whichWeekDay()


