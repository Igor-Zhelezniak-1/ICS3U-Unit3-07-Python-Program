#!/usr/bin/env python3

# Created by: Igor
# Created on: Sept 2021
# This is game


def main():
    # this function uses a try statement

    # input
    integer1 = input("Enter your age(use numbers): ")
    integer2 = input("Are you really good loking (1-yes or 0-no): ")
    integer3 = input("Are you rich (1-yes or 0-no): ")
    print("")

    # process & output
    try:
        age = int(integer1)
        loking = int(integer2)
        rich = int(integer3)
        if loking > 1:
            print("Please follow the instructions! You need to enter 1 or 0")
        elif loking < 0:
            print("Please follow the instructions! You need to enter 1 or 0")
        elif rich > 1:
            print("Please follow the instructions! You need to enter 1 or 0")
        elif rich < 0:
            print("Please follow the instructions! You need to enter 1 or 0")
        else:
            if (
                age > 25
                and age < 40
                and loking == 1
                or rich == 1
                and age > 25
                and age < 40
            ):
                print("Both grandmothets will say:")
                print("You are accepted to date my grandchild!")
                print("You can choose!")
            elif age > 40 and loking == 1 or rich == 1 and age > 40:
                print("Grandmother#1 will say:")
                print("You are too old!")
                print("Grandmother#2 will say:")
                print("You are accepted to date my grandchild!")
            elif age < 25 and loking == 1 or rich == 1 and age < 25:
                print("Grandmother#1 will say:")
                print("You are too young!")
                print("Grandmother#2 will say:")
                print("You are accepted to date my grandchild!")
            elif age > 25 and age < 40 and loking != 1 and rich != 1:
                print("Grandmother#1 will say:")
                print("You are accepted to date my grandchild!")
                print("Grandmother#2 will say:")
                print("Sorry, but you not rich or good lokind!")
            else:
                print("Both grandmothets will say:")
                print("Sorry, you can't")

    except Exception:
        print("Please follow the instructions! Use numbers")
    finally:
        print("Good luck!")


if __name__ == "__main__":
    main()
