
with open('input.txt') as f:
    lines = f.readlines()

# print(lines)

#convert input into an array
original_program = lines[0].strip().split(',')

#convert strings to integers
original_program = [int(num) for num in original_program]
# print(program)


#use brute-force approach to go through every combination of 0 through 100 for position 1 and 2



for noun in range(0,100):
    
    for verb in range(0,100):

        program = original_program.copy()
        program[1] = noun
        program[2] = verb

        #iterate through the program, starting at index 0 
        i = 0
        while True:
            if program[i] == 1:
                # print('add')
                first_position = program[i + 1]
                second_position = program[i + 2]
                final_position = program[i + 3]
                program[final_position] = program[first_position] + program[second_position]
                i += 4
            elif program[i] == 2:
                # print('multiply')
                first_position = program[i + 1]
                second_position = program[i + 2]
                final_position = program[i + 3]
                program[final_position] = program[first_position] * program[second_position]
                i += 4
            elif program[i] == 99:
                # print('halt')
                break
            else:
                # print('error')
                # print("i: " + str(i))
                # print(program[i])
                # print("j: " + str(j))
                # print("k: " + str(k))

                break

        if program[0] == 19690720:
            print(noun)
            print(verb)

            print("answer:" + str(100 * noun + verb))