data = open('./data.txt').read()

sum = 0
for line in data.splitlines():
    digit = ''
    for character in line:
        if(character.isdigit()):
            digit += character
    digit = int(digit[0] + digit[-1])
    sum += digit

print(sum)