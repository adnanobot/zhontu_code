"""
Author: Zhontu Mia
This program takes choices from the user and calculates area of different geometric bodies.
"""
import math


def get_triangle_area():
    print("\nCalculating area of a triangle")


def get_square_area():
    print("\nCalculating area of a square")


def get_rectangle_area():
    print("\nCalculating area of a rectangle")


def get_circle_area():
    print("\nCalculating area of a circle")

    radius = input("Please enter radius of the circle: ")
    # Remember that, the function- input() always returns a string.
    # Therefore, we must convert it to an integer or floating point number.

    radius = float(radius)
    area = 2 * math.pi * (radius)**2

    print("\nArea of the circle is: ", area)

    # The following things, we can implement together inshaAllah
    # TODO: 1. Verify the result
    # TODO: 2. Specify unit of radius - cm or m
    # TODO: 3. Check for invalid input from the user
    # TODO: 4. Format the output to up to two decimal places. Now it is too big and does not look nice.


# when you run the script the program will start from here
if __name__ == "__main__":
    print("Area calculator.")
    print("This program calculates area of different geometric shapes")
    print("==========================================================")
    print("Operations: Calculate area of - ")
    print("[1]. Circle.")
    print("[2]. Rectangle.")
    print("[3]. Square.")
    print("[4]. Triangle(right-angle)")

    user_choice = input("\nPlease select an operation from above:  ")

    if user_choice == '1':
        get_circle_area()
        # Now the program will go to the function
    elif user_choice == '2':
        get_square_area()
    elif user_choice == '3':
        get_rectangle_area()
    else:
        get_triangle_area()
