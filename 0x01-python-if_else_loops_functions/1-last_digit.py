#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if number < 0:
    last_digit = -last_digit
if last_digit > 5:
    val = "and is greaterthan"
elif last_digit == 0:
    val = "and is 0"
else:
    val = "and is lessthan 6 and not 0"
print("Last digit of {:d} is {:d} {:s}".format(number, last_digit, val))
