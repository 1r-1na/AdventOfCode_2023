data = open('./day_3/data.txt').readlines()


def is_part_number(positions_to_check: list, lines: list, on_left: bool, on_right: bool):
    if not on_left:
        positions_to_check.insert(0, positions_to_check[0] - 1)
    if not on_right:
        positions_to_check.append(positions_to_check[-1] + 1)
    for li in lines:
        characters_to_check = li[positions_to_check[0]:positions_to_check[-1] + 1]
        if any(not c.isdigit() and not c == '.' for c in characters_to_check):
            return True
    return False


part_numbers_sum = 0

positions = []
last_index_data = len(data) - 1

for line_index, line in enumerate(data):
    last_line_index = len(line) - 1
    for char_index, character in enumerate(line):
        if char_index == last_line_index:
            continue

        if character.isdigit():
            positions.append(char_index)

        if (line[char_index + 1] == '\n' or not line[char_index + 1].isdigit()) and len(positions) > 0:
            # number detected
            lines_to_check = []
            if line_index != 0:
                lines_to_check.append(data[line_index - 1])
            lines_to_check.append(line)
            if line_index != last_index_data:
                lines_to_check.append(data[line_index + 1])

            if is_part_number(positions.copy(), lines_to_check, on_left=(positions[0] == 0),
                              on_right=(line[char_index + 1] == '\n')):
                # part number detected
                n = line[positions[0]:positions[-1] + 1]
                part_numbers_sum += int(n)
            positions.clear()

print("Sum of all part numbers:", part_numbers_sum) # 546312
