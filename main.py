print("Hello To school coding projects")
Input = int(input("(Enter the values in numberPLs select the program:\n"
                  "1) Program one(Find the sum of numbers)\n"
                  "2) Program two(Use to swap values of two numbers)\n"
                  "3) Program three(finds the area and perimeter of a square)\n"
                  "4) Program four(finds the area and perimeter of a rectangle)\n"
                  "5) Program five (finds is the pin entered by the user is four digits)\n"
                  "6) Program six (finds is the batsman has scored a century or not)\n"
                  "Enter the number: "))

if Input == 1:
    print("Program begins")
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("The sum of both the number is ", a + b)
    print("Program has ended")

elif Input == 2:
    print("Program begins")
    ab = int(input("Enter the value of ab: "))
    bc = int(input("Enter the value of bc: "))
    ab , bc = bc , ab
    print("The value ab after swapping is ",ab )
    print("The value ab after swapping is ", bc )
    print("Program has ended")

elif Input == 3:
    print("Program begins")
    s = int(input("Enter the length of a side of the square: "))
    print("The perimeter of the square is ",s * 4 )
    print("The area of the square is ", s * s)
    print("Program has ended")

elif Input == 4:
    print("Program begins")
    l = int(input("Enter the length of the rectangle: "))
    br = int(input("Enter the breath of the rectangle: "))
    print("The perimeter of the rectangle is ", l * 2 + br * 2)
    print("The area of the rectangle is ", l * br)
    print("Program has ended")

elif Input == 5:
    print("Program begins")
    pin = int(input("Pls enter the pin:\n "))
    if pin in range(1000, 10000):
        print("The pin looks good")
        print("Your pin is saved successfully.")
    else:
        print("Pls rerun the program and enter a pin that is 4 digits.")

elif Input == 6:
    print("Program begins")
    runs = int(input("Enter the runs scored by the batsman: \n "))
    if runs >= 100:
        print("The player has scored the century.")
    else:
        print("The player has not scored the century yet , :( But keep cheering!")

else:
    print("Pls enter the correct number.")
