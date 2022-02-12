#Fibbonacci

import math

first = 1
count = 1

while (count == 1) or (count == 2):
    second = first
    print(second)
    count += 1

while count > 2:
    third = first + second
    print(third/second)
    first = second
    second = third
