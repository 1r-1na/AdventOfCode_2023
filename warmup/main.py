data = open('./data.txt').read()

floor = 0
position = 0
first_time_basement = 0
found = False
for c in data:
    if c == '(':
        floor += 1
    elif c == ')':
        floor -= 1
    position += 1
    if(not found and floor == -1):
        first_time_basement = position
        found = True

print("Floor:", floor)
print("Position of entering basement for the first time:", first_time_basement)