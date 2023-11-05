import random

while True:
    number = str(random.randint(10000,99999))
    first_ones = int(number[0])+int(number[1])+int(number[2])
    last_ones = int(number[3])+int(number[4])
    if first_ones == last_ones:
        print(number,"Correct verification",first_ones,"=",last_ones)
        break
    elif first_ones != last_ones:
        print(number,"invalid verification",first_ones,"!=",last_ones)
        continue