#!/usr/bin/env python3
# Created by: Navin Balekomebole
# Created on: Dec 1st, 2021
# This program asks the user for the diameter of the
# pizza. It then calculates and displays the total cost
# of the pizza with tax
import constants


def main():
    # input
    diameter = int(input("Enter the diameter of the pizza (inches): "))

    # process
    subtotal = constants.LABOUR + constants.RENTAL + constants.INGR * diameter
    tax = constants.HST * subtotal
    total = subtotal + tax

    # output
    print("")
    print("The total cost is = ${:,.2f}".format(total))


if __name__ == "__main__":
    main()
