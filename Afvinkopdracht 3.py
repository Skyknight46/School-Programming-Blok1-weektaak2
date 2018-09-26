 #!/usr/bin/env/python3

import easygui

#1 Number analyzer
print("\n")
nummer = int(input("Give a number "))
if nummer > 0:
    print("Positive")
elif nummer < 0:
    print("Negative")
else:
    print("Zero")

if nummer % 2 == 0:
    print("Even")
else:
    print("Odd")

#2 Area's of rectangles
print("\n")
lenrect1 = float(input("Give the LENGTH of the first rectangle "))
widthrect1 = float(input("Give the WIDTH of the first rectangle "))
lenrect2 = float(input("Give the LENGTH of the second rectangle "))
widthrect2 = float(input("Give the WIDTH of the second rectangle "))

aRect1 = lenrect1 * widthrect1
aRect2 = lenrect2 * widthrect2

if aRect1 > aRect2:
    print("The first rectangle was larger than the second")
elif aRect2 > aRect1:
    print("The second rectangle was larger than the first")
else:
    print("The rectangles are both equal in size")

#9 Roulette wheel colors
print("\n")

pocket0 = 0
lijstoneven = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
lijsteven = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

pocketnummer = int(input("Give a pocketnumber \n"))

if pocketnummer in lijstoneven:
    print("The color of the entered pocket is RED")
elif pocketnummer == pocket0:
    print("The color of the entered pocket is GREEN")
elif pocketnummer in lijsteven:
    print("The color of the entered pocket is BLACK")
else:
    print("The entered number is outside the range of the roulette wheel")

#17 Wi-Fi diagnostic Tree
print("\n")
print("Reboot the pc and try to connect")
problem1 = input("did that fix the problem?\n")
if problem1 == "y":
    print("Fixed")
else:
    print("Reboot the router and try to connect")
    Problem2 = input("Did this fix your problem?\n")
    if Problem2 == "y":
        print("Fixed")
    else:
        print("Make sure the cables between the router and modem are plugged in firmly")
        Problem3 = input("Did this fix your problem?\n")
        if Problem3 == "y":
            print("Fixed")
        else:
            print("Move the router to a new location")
            Problem4 = input("Did this fix your problem?\n")
            if Problem4 == "y":
                print("GET A NEW ROUTER")
            else:
                print("GET A NEW ROUTER")
            
#18 Restaurant selector
print("\n")

vegan = input("Is anyone in your party vegan?\n")
vegetarian = input("Is anyone in your party vegetarian?\n")
gluten_free = input("Is anyone in your party gluten free\n")

if vegan == "y" and vegetarian == "y" and gluten_free == "y":
    print("Your options are:\nCorner Café\nThe chef's kitchen")
elif vegan == "y" and vegetarian == "y" and gluten_free == "n":
    print("Your options are:\nCorner Café\nThe chef's kitchen")
elif vegan == "y" and vegetarian == "n" and gluten_free == "y":
    print("Your options are:\nMain street pizza company\nCorner café\nThe chef's kitchen")
elif vegan == "y" and vegetarian == "n" and gluten_free == "n":
    print("Your options are:\nMain street pizza company\nCorner café\nThe chef's kitchen")
elif vegan == "n" and vegetarian == "n" and gluten_free == "n":
    print("Your options are:\nJoe's gourmet burgers\nMain street pizza company\nCorner café\nMama's fine italian\nThe chef's kitchen")
elif vegan == "n" and vegetarian == "n" and gluten_free == "y":
    print("Your options are:\nMain street pizza company\nCorner café\nThe chef's kitchen")
elif vegan == "n" and vegetarian == "y" and gluten_free == "n":
    print("Your options are:\nMain street pizza company\nCorner café\nMama's fine italian\nThe chef's kitchen")
else:
    print("ERROR 404. FILE NOT FOUND")
