#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10  # Get the last digit, handle negative numbers using abs()
    print("{}".format(last_digit), end="")  # Print the last digit
    return last_digit  # Return the last digit
