#!/usr/bin/env python3

# Created by: Andrei Chirilov
# Created on: November 2019
# This program calculates the rounded off number to a decimal place


def rounding(number, rounder):
    # This function rounds the user's number to what they choose

    # Process
    rounded_number = (number[0]*(10**rounder))
    rounded_number = rounded_number + 0.5
    rounded_number = int(rounded_number)
    rounded_number = rounded_number/(10**rounder)

    return rounded_number


def main():
    # This function takes the user's number then outputs the number rounded

    # rounder list
    rounding_number = []

    # Process
    while True:
        decimal = input("Enter the decimal number you wish to be rounded: ")
        rounder = input("Enter how many decimal places you want rounded: ")

        try:
            decimal = float(decimal)
            rounder = int(rounder)
            rounding_number.append(decimal)
            if decimal == float(decimal) and \
               rounder == int(rounder):
                rounded_dec = rounding(rounding_number, rounder)
                print("")
                print("The result is: ", rounded_dec)
                break
            else:
                print("Not a valid input.")
        except Exception:
            print("Please input a valid input.")
            print("")


if __name__ == "__main__":
    main()
