import sys


def solve(lines):
    numbers = {
    }
    symbols = {}
    for index, line in enumerate(lines):
        number = ''
        for i, character in enumerate(line):
            if character == '.':
                if number != '':
                    numbers[((index,i-len(number)), (index,i-1))] =int(number)
                    number = ''
                continue
            elif character >= '0' and character <= '9':
                number += character
            elif character =='\n':
                if number != '':
                    numbers[((index,i-len(number)), (index,i-1))] =int(number)
                    number = ''
            else:
                symbols[(index, i)] = character
    selected_numbers = []
    selected_positions = {}
    for key_symbol in symbols:
        x,y = key_symbol
        for key_number in numbers:
            if key_number in selected_positions:
                continue
            sx,sy = key_number[0]
            ex,ey = key_number[1]
            if (x-1 >= sx and x-1 <= ex) and (y+1 >= sy and y+1 <= ey):
                selected_positions[key_number] = 0
                selected_numbers.append(numbers[key_number])
            elif (x >= sx and x <= ex) and (y+1 >= sy and y+1 <= ey):
                selected_positions[key_number] = 0
                selected_numbers.append(numbers[key_number])
            elif (x+1 >= sx and x+1 <= ex) and (y+1 >= sy and y+1 <= ey):
                selected_positions[key_number] = 0
                selected_numbers.append(numbers[key_number])
            elif (x+1 >= sx and x+1 <= ex) and (y >= sy and y <= ey):
                selected_positions[key_number] = 0
                selected_numbers.append(numbers[key_number])
            elif (x+1 >= sx and x+1 <= ex) and (y-1 >= sy and y-1 <= ey):
                selected_positions[key_number] = 0
                selected_numbers.append(numbers[key_number])
            elif (x >= sx and x <= ex) and (y-1 >= sy and y-1 <= ey):
                selected_positions[key_number] = 0
                selected_numbers.append(numbers[key_number])
            elif (x-1 >= sx and x-1 <= ex) and (y-1 >= sy and y-1 <= ey):
                selected_positions[key_number] = 0
                selected_numbers.append(numbers[key_number])
            elif (x-1 >= sx and x-1 <= ex) and (y >= sy and y <= ey):
                selected_positions[key_number] = 0
                selected_numbers.append(numbers[key_number])
                x=10
    print(len(selected_positions), selected_positions) 
    print(len(selected_numbers), selected_numbers) 
    return sum(list(set(selected_numbers)) )
lines = open(sys.argv[1]).readlines()
print(solve(lines))
