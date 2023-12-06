import math

data = open('./data.txt').readlines()

numbers = []
stars = []

number = 0
char_positions = []
for line_index, line in enumerate(data):
    for char_index, char in enumerate(line):
        if char.isdigit():
            number = (10 * number) + int(char)
            char_positions.append(char_index)
        else:
            if number > 0:
                numbers.append((line_index, char_positions, number))
            if char == '*':
                stars.append((line_index, char_index))
            number = 0
            char_positions = []


offsets = [[-1, -1], [-1, 0], [-1, 1], [1, -1], [1, 0], [1, 1]]

gear_ratio_total = 0

possible_gear_numbers = {}
for star_pos in stars:
    for num_pos in numbers:
        for offset in offsets:
            pos_to_check = [star_pos[0] + offset[0], star_pos[1] + offset[1]]
            if pos_to_check[0] == num_pos[0] and pos_to_check[1] in num_pos[1]:
                # possible gear found
                key = str(num_pos[0]) + str(num_pos[1])
                possible_gear_numbers[key] = num_pos[2]
    if len(possible_gear_numbers) == 2:
        gear_ratio_total += math.prod(possible_gear_numbers.values())
    possible_gear_numbers = {}

print("Gear ratio total:", gear_ratio_total)

#12409965
#85155778 too low
#68208793
#68208793



