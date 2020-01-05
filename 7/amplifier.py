class Amplifier:
    def __init__(self):
        # filename = 'input.txt'
        filename = 'input.txt'

        with open(filename) as f:
            lines = f.readlines()

        program = lines[0].strip().split(',')
        program = [int(num) for num in program]

        #for debugging purposes
        # program = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]

        self.program = program
        self.i = 0
        self.input_count = 0

    def run(self, phase, my_input):
        # print(self.program)

        while True:
            # print("     i:{}".format(self.i))
            # print("     {}:{}".format(self.program[self.i], type(self.program[self.i])))
            # print("i:{}, self.program[self.i]:{}".format(i, self.program[self.i]))
            if self.program[self.i] % 100 == 1:
                # print('add')
                first_position = self.program[self.i + 1]
                second_position = self.program[self.i + 2]
                final_position = self.program[self.i + 3]
                #(self.program[self.i] // 100) % 10 corresponds to first parameter
                 #(self.program[self.i] // 100)// 10 corresponds to second parameter
                if ((self.program[self.i] // 100) % 10) == 0 and ((self.program[self.i] // 100) // 10) == 0:   
                    self.program[final_position] = self.program[first_position] + self.program[second_position]
                elif ((self.program[self.i] // 100) % 10) == 1 and ((self.program[self.i] // 100)// 10) == 1:
                    self.program[final_position] = self.program[self.i + 1] + self.program[self.i + 2]
                    # print("entered correct if statement")
                elif ((self.program[self.i] // 100) % 10) == 1 and ((self.program[self.i] // 100)// 10) == 0:
                    self.program[final_position] = self.program[self.i + 1] + self.program[second_position]
                elif ((self.program[self.i] // 100) % 10) == 0 and ((self.program[self.i] // 100)// 10) == 1:
                    self.program[final_position] = self.program[first_position] + self.program[self.i + 2]
                self.i += 4


            elif self.program[self.i] % 100 == 2:
                # print('multiply')
                first_position = self.program[self.i + 1]
                second_position = self.program[self.i + 2]
                final_position = self.program[self.i + 3]
                if ((self.program[self.i] // 100) % 10) == 0 and ((self.program[self.i] // 100) // 10) == 0:   
                    self.program[final_position] = self.program[first_position] * self.program[second_position]
                elif ((self.program[self.i] // 100) % 10) == 1 and ((self.program[self.i] // 100)// 10) == 1:
                    self.program[final_position] = self.program[self.i + 1] * self.program[self.i + 2]
                    # print("entered correct if statement")
                elif ((self.program[self.i] // 100) % 10) == 1 and ((self.program[self.i] // 100)// 10) == 0:
                    self.program[final_position] = self.program[self.i + 1] * self.program[second_position]
                elif ((self.program[self.i] // 100) % 10) == 0 and ((self.program[self.i] // 100)// 10) == 1:
                    self.program[final_position] = self.program[first_position] * self.program[self.i + 2]

                self.i += 4

            elif self.program[self.i] % 100 == 3:
                position = self.program[self.i + 1]
                self.program[position] = phase if self.input_count == 0 else my_input
                self.input_count += 1
                self.i += 2

            elif self.program[self.i] % 100 == 4:
                position = self.program[self.i + 1]
                value = self.program[position] if (self.program[self.i] // 100) % 10 == 0 else self.program[self.i + 1]
                self.i += 2
                return value
                

            elif self.program[self.i] % 100 == 5:
                value1 = self.program[self.i + 1] if ((self.program[self.i] // 100) % 10 == 1) else self.program[self.program[self.i + 1]] 
                value2 = self.program[self.i + 2] if (self.program[self.i] // 100) // 10 == 1 else self.program[self.program[self.i + 2]] 
                if value1 != 0:
                    self.i = value2
                else:
                    self.i += 3

            elif self.program[self.i] % 100 == 6:
                value1 = self.program[self.i + 1] if ((self.program[self.i] // 100) % 10 == 1) else self.program[self.program[self.i + 1]] 
                value2 = self.program[self.i + 2] if ((self.program[self.i] // 100) // 10 == 1) else self.program[self.program[self.i + 2]] 
                if value1 == 0:
                    self.i = value2
                else:
                    self.i += 3

            elif self.program[self.i] % 100 == 7:
                value1 = self.program[self.i + 1] if ((self.program[self.i] // 100) % 10 == 1) else self.program[self.program[self.i + 1]] 
                value2 = self.program[self.i + 2] if ((self.program[self.i] // 100) // 10 == 1) else self.program[self.program[self.i + 2]]
                # print("3rd parameter: {}".format(self.program[self.i + 3]))
                self.program[self.program[self.i + 3]] = 1 if value1 < value2 else 0
                self.i += 4
                    

            elif self.program[self.i] % 100 == 8:
                value1 = self.program[self.i + 1] if ((self.program[self.i] // 100) % 10 == 1) else self.program[self.program[self.i + 1]] 
                value2 = self.program[self.i + 2] if ((self.program[self.i] // 100) // 10 == 1) else self.program[self.program[self.i + 2]]
                self.program[self.program[self.i + 3]] = 1 if value1 == value2 else 0
                self.i += 4

            elif self.program[self.i] % 100 == 99:
                # print('halt')
                break
            else:
                print('error')
                break

        return "Halted"
