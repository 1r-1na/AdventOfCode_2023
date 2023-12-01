data = open('./data.txt').read()

def calibrate(input):
    sum = 0
    for line in input.splitlines():
        digit = ''
        for character in line:
            if(character.isdigit()):
                digit += character
        digit = int(digit[0] + digit[-1])
        sum += digit
    return sum


result = calibrate(data)
print("First result:", result)

data_mapped = data.replace('one', 'o1e').replace('two', 't2o').replace('three', 't3e').replace('four', 'f4r').replace('five', 'f5e').replace('six', 's6x').replace('seven', 's7n').replace('eight', 'e8t').replace('nine', 'n9e')

result_corrected = calibrate(data_mapped)
print("Second result:", result_corrected)

