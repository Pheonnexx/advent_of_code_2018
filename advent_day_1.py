
total = 0
frequency_set = set()
first_freq = 0
freq_dup_match = False

while freq_dup_match == False:
    with open('advent_day_1_data.txt', 'r') as file:
        data =  file.readlines()
        for line in data:
            number = int(line[1:].rstrip())
            if line[0] == '+':
                total = total + number
            else:
                total = total - number
            if total not in frequency_set:
                frequency_set.add(total)
            else:
                first_freq = total
                freq_dup_match = True

print(first_freq)