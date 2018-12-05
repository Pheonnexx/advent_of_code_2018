from collections import Counter

two_letters = 0
three_letters = 0

with open('advent_day_2.txt', 'r') as file:
    data =  file.readlines()
    for line in data:
        counted_letters = Counter(line)
        for key, value in counted_letters.items():
            if value == 3:
                 three_letters =+ 1
            elif value == 2:
                two_letters =+ 1

print(two_letters)
print(three_letters)