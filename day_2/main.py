data = open('./data.txt').readlines()

max_red = 12
max_green = 13
max_blue = 14

def getDigit(s: str):
    r = ''
    for c in s:
        if(c.isdigit()):
            r += c
    return int(r)

# { game_id: [red, green, blue, possible] }
result = {}

for line in data:
    splittedLine = line.split(':')
    game_id = int(splittedLine[0][5:])
    splitted_subsets = splittedLine[1].split(';')
    result[game_id] = [0, 0, 0, True]
    for subset in splitted_subsets:
        num_colors = subset.split(',')
        for num_color in num_colors:
            if('red' in num_color):
                count = getDigit(num_color)
                if(count > max_red):
                    result[game_id][3] = False
                if(result[game_id][0] < count):
                    result[game_id][0] = count
            if('green' in num_color):
                count = getDigit(num_color)
                if(count > max_green):
                    result[game_id][3] = False
                if(result[game_id][1] < count):
                    result[game_id][1] = count
            if('blue' in num_color):
                count = getDigit(num_color)
                if(count > max_blue):
                    result[game_id][3] = False
                if(result[game_id][2] < count):
                    result[game_id][2] = count

def filter_possible(pair):
    return pair[1][3] # True if possible, False if not

possible_games = dict(filter(filter_possible, result.items()))
print("All possible game id's summed up:", sum(possible_games.keys()))

sum_power_of_minimum_sets = 0
for set in result.values():
    sum_power_of_minimum_sets += set[0] * set[1] * set[2]

print("All powers of the minimum set per game summed up:", sum_power_of_minimum_sets)
