filename = 'input.txt'

with open(filename) as f:
    lines = f.readlines()

# print(len(lines))

#separate the string into a list of each instruction
# print(lines[0])
program = lines[0].strip().split(',')
# print(program)
program = [int(num) for num in program]

# program = [1104, 2, 99]



i = 0
while True:
    # print(program[i] % 100)
    # break
    # print("     {}:{}".format(program[i], type(program[i])))
    if program[i] % 100 == 1:
        print('add')
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

        #this should print 7
        # print(program[0])
        i += 4


    elif program[i] % 100 == 2:
        print('multiply')
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
       
        #this should print 12
        # print(program[0])
        i += 4

    elif program[i] % 100 == 3:
        user_input = input("Enter a number: ")
        position = program[i + 1]
        program[position] = int(user_input)
        i += 2

    elif program[i] % 100 == 4:
        position = program[i + 1]
        value = program[position] if (program[i] // 100) % 10 == 0 else program[i + 1]
        #output the value of its only parameter
        #should output 2
        print(value)
        i += 2

    elif program[i] % 100 == 99:
        print('halt')
        break
    else:
        print('error')
        break




    