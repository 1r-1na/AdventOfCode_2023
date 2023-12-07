import re

data = open('./data.txt').readlines()


def parse_line(li: str):
    line_split = li.split('|')

    x = re.sub(r'^Card.*:', '', line_split[0], 1).split(' ')
    x = filter(lambda n: n != '', x)
    winning_numbers = list(map((lambda n: int(n)), x))

    y = line_split[1].split(' ')
    y = filter(lambda n: n != '', y)
    actual_numbers = list(map((lambda n: int(n)), y))

    return winning_numbers, actual_numbers


def part_1():
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
    return total


def part_2():
    collected_cards = {}
    last_index = len(data) - 1
    for index, line in enumerate(data):
        wn, an = parse_line(line)
        # add original card
        if index in collected_cards:
            collected_cards[index] = collected_cards[index] + 1
        else:
            collected_cards[index] = 1
        count_cards_at_index = collected_cards[index]
        count_matching_numbers = 0
        for actual_number in an:
            if actual_number in wn:
                count_matching_numbers += 1
        for i in range(count_matching_numbers):
            next_index = index + i + 1
            if next_index > last_index:
                break
            if next_index in collected_cards:
                collected_cards[next_index] = collected_cards[next_index] + count_cards_at_index
            else:
                collected_cards[next_index] = count_cards_at_index

    return sum(collected_cards.values())


print("Points worth in total:", part_1())  # 26346
print("Total scratchcards:", part_2())  # 8467762
