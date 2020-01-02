
with open('input.txt') as f:
    lines = f.readlines()

# print(lines)

#convert input into an array
program = lines[0].strip().split(',')

#convert strings to integers
program = [int(num) for num in program]
# print(program)


#iterate through the program, starting at index 0 

program[1] = 12
program[2] = 2

i = 0
while True:
    if program[i] == 1:
        print('add')
        first_position = program[i + 1]
        second_position = program[i + 2]
        final_position = program[i + 3]
        program[final_position] = program[first_position] + program[second_position]
        i += 4

    elif program[i] == 2:
        print('multiply')
        first_position = program[i + 1]
        second_position = program[i + 2]
        final_position = program[i + 3]
        program[final_position] = program[first_position] * program[second_position]
        i += 4
    elif program[i] == 99:
        print('halt')
        break
    else:
        print('error')
        break

print(program[0])





