#!/usr/bin/env python3
# Created By: Redd Forfieda
# Date: Nov 23, 2023
# this program uses a fuction to covert Fahrenheit and celsius
def fahrenheit():
    user_celsius = input("enter your celsius ")
    try:
        user_celsius = float(user_celsius)
    except ValueError:
        print("your number invalid")
    else:
        user_tempf = round((user_celsius * 9 / 5) + 32, 2)
        print(f"{user_celsius} is equal to {user_tempf}F")


def main():
    fahrenheit()


if __name__ == "__main__":
    main()
