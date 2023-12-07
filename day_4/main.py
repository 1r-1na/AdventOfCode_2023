import re

data = open('./data.txt').readlines()


def parse_line(l: str):
    line_split = l.split('|')

    x = re.sub(r'^Card.*:', '', line_split[0], 1).split(' ')
    x = filter(lambda n: n != '', x)
    winning_numbers = list(map((lambda n: int(n)), x))

    y = line_split[1].split(' ')
    y = filter(lambda n: n != '', y)
    actual_numbers = list(map((lambda n: int(n)), y))

    return winning_numbers, actual_numbers


total = 0
for line in data:
    point = 0
    wn, an = parse_line(line)
    for current_num in an:
        if current_num in wn:
            if point > 0:
                point += point
            else:
                point = 1
    total += point

print("Points worth in total:", total) # 26346
