#!/usr/bin/env python3

number = int(input("Enter a number:\n"))

for multiplier in range(1, 9):
    print(f"{number} x {multiplier} = {number * multiplier}")