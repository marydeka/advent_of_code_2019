import copy


filename = 'input.txt'

with open(filename) as f:
    lines = f.readlines()

#separate the string into a list of each instruction
program = lines[0].strip().split(',')
# print(program)
program = [int(num) for num in program]

# program = [1105, 9, 3, 1101, 3, 4, 0, 99]

my_list = [0,1,2,3,4]

permutations = [[]]

for i in my_list:
    new_permutations = []
    # new_list = [i]
    # permutations.append(new_list)
    for perm in permutations:
        for j in my_list:
            if j in perm:
                continue
            else:
                new_perm = copy.deepcopy(perm)
                new_perm.append(j)
                new_permutations.append(new_perm)
    permutations = new_permutations

def find_output(phase, my_input):
    i = 0
    input_count = 0
    while True:
        # print("     {}:{}".format(program[i], type(program[i])))
        # print("i:{}, program[i]:{}".format(i, program[i]))
        if program[i] % 100 == 1:
            # print('add')
            first_position = program[i + 1]
            second_position = program[i + 2]
            final_position = program[i + 3]
            #(program[i] // 100) % 10 corresponds to first parameter
             #(program[i] // 100)// 10 corresponds to second parameter
            if ((program[i] // 100) % 10) == 0 and ((program[i] // 100) // 10) == 0:   
                program[final_position] = program[first_position] + program[second_position]
            elif ((program[i] // 100) % 10) == 1 and ((program[i] // 100)// 10) == 1:
                program[final_position] = program[i + 1] + program[i + 2]
                # print("entered correct if statement")
            elif ((program[i] // 100) % 10) == 1 and ((program[i] // 100)// 10) == 0:
                program[final_position] = program[i + 1] + program[second_position]
            elif ((program[i] // 100) % 10) == 0 and ((program[i] // 100)// 10) == 1:
                program[final_position] = program[first_position] + program[i + 2]
            i += 4


        elif program[i] % 100 == 2:
            # print('multiply')
            first_position = program[i + 1]
            second_position = program[i + 2]
            final_position = program[i + 3]
            if ((program[i] // 100) % 10) == 0 and ((program[i] // 100) // 10) == 0:   
                program[final_position] = program[first_position] * program[second_position]
            elif ((program[i] // 100) % 10) == 1 and ((program[i] // 100)// 10) == 1:
                program[final_position] = program[i + 1] * program[i + 2]
                # print("entered correct if statement")
            elif ((program[i] // 100) % 10) == 1 and ((program[i] // 100)// 10) == 0:
                program[final_position] = program[i + 1] * program[second_position]
            elif ((program[i] // 100) % 10) == 0 and ((program[i] // 100)// 10) == 1:
                program[final_position] = program[first_position] * program[i + 2]

            i += 4

        elif program[i] % 100 == 3:
            position = program[i + 1]
            program[position] = phase if input_count == 0 else my_input
            input_count += 1
            i += 2

        elif program[i] % 100 == 4:
            position = program[i + 1]
            value = program[position] if (program[i] // 100) % 10 == 0 else program[i + 1]
            return value
            i += 2

        elif program[i] % 100 == 5:
            value1 = program[i + 1] if ((program[i] // 100) % 10 == 1) else program[program[i + 1]] 
            value2 = program[i + 2] if (program[i] // 100) // 10 == 1 else program[program[i + 2]] 
            if value1 != 0:
                i = value2
            else:
                i += 3

        elif program[i] % 100 == 6:
            value1 = program[i + 1] if ((program[i] // 100) % 10 == 1) else program[program[i + 1]] 
            value2 = program[i + 2] if ((program[i] // 100) // 10 == 1) else program[program[i + 2]] 
            if value1 == 0:
                i = value2
            else:
                i += 3

        elif program[i] % 100 == 7:
            value1 = program[i + 1] if ((program[i] // 100) % 10 == 1) else program[program[i + 1]] 
            value2 = program[i + 2] if ((program[i] // 100) // 10 == 1) else program[program[i + 2]]
            # print("3rd parameter: {}".format(program[i + 3]))
            program[program[i + 3]] = 1 if value1 < value2 else 0
            i += 4
                

        elif program[i] % 100 == 8:
            value1 = program[i + 1] if ((program[i] // 100) % 10 == 1) else program[program[i + 1]] 
            value2 = program[i + 2] if ((program[i] // 100) // 10 == 1) else program[program[i + 2]]
            program[program[i + 3]] = 1 if value1 == value2 else 0
            i += 4

        elif program[i] % 100 == 99:
            print('halt')
            break
        else:
            print('error')
            break
    # print(program[0])

final_outputs = []

for perm in permutations:
    A = find_output(perm[0], 0)
    B = find_output(perm[1], A)
    C = find_output(perm[2], B)
    D = find_output(perm[3], C)
    E = find_output(perm[4], D)
    final_outputs.append(E)

print(max(final_outputs))



    