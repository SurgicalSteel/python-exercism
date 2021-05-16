import math

def is_armstrong_number(number):
    rawNumber = format(f"{number}")
    numDigit = len(rawNumber)
    total = 0
    for i in rawNumber:
        total += math.pow(int(i),numDigit)
    return total == number
