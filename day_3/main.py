import numpy as np

data = open('./day_3/data.txt').readlines()

# lines: [ [......458....#],
#          [....456+.....#],
#          [......#.893...] ]
#
# number_positions: [6, 7, 8]
#
def is_part_number(number_positions: list, lines: np.array, isFirstLine = False, isLastLine = False):
    current_line_index = 1
    if isFirstLine:
        current_line_index = 0
    line_length = len(lines[current_line_index])
    # check left side
    if number_positions[0] > 0:
        if lines[current_line_index][number_positions[0] - 1] != '.' and not lines[current_line_index][number_positions[0] - 1].isdigit():
            return True
    # check right side
    if number_positions[-1] < line_length - 1:
        if lines[current_line_index][number_positions[-1] + 1] != '.' and not lines[current_line_index][number_positions[-1] + 1].isdigit():
            return True
    # check above
    if not isFirstLine:
        for num_pos in number_positions:
            if lines[current_line_index - 1][num_pos] != '.' and not lines[current_line_index - 1][num_pos].isdigit():
                return True
        # check left diagonal
        if number_positions[0] > 0:
            if lines[current_line_index - 1][number_positions[0] - 1] != '.' and not lines[current_line_index - 1][number_positions[0] - 1].isdigit():
                return True
        # check right diagonal
        if number_positions[-1] < line_length - 1:
            if lines[current_line_index - 1][number_positions[-1] + 1] != '.' and not lines[current_line_index - 1][number_positions[-1] + 1].isdigit():
                return True
    # check below
    if not isLastLine:
        for num_pos in number_positions:
            if lines[current_line_index + 1][num_pos] != '.' and not lines[current_line_index + 1][num_pos].isdigit():
                return True
        # check left diagonal
        if number_positions[0] > 0:
            if lines[current_line_index + 1][number_positions[0] - 1] != '.' and not lines[current_line_index + 1][number_positions[0] - 1].isdigit():
                return True
        # check right diagonal
        if number_positions[-1] < line_length - 1:
            if lines[current_line_index + 1][number_positions[-1] + 1] != '.' and not lines[current_line_index + 1][number_positions[-1] + 1].isdigit():
                return True
    return False

part_numbers_sum = 0

# index for a line
for i, line in enumerate(data):
    positions = []
    number_detected = False
    for j, character in enumerate(line):
        if number_detected:
            part_number = False
            if i == 0:
                part_number = is_part_number(positions, np.array([line, data[i + 1]]), isFirstLine=True)
            elif i == len(data) - 1:
                part_number = is_part_number(positions, np.array([data[i - 1], line]), isLastLine=True)
            else:
                part_number = is_part_number(positions, np.array([data[i - 1], line, data[i + 1]]))
            if part_number:
                part_numbers_sum += int(line[positions[0]:(positions[-1]+1)])
            number_detected = False
            positions = []
        if character.isdigit():
            positions.append(j)
        elif len(positions) > 0:
           number_detected = True

print("Sum of all part numbers:", part_numbers_sum)