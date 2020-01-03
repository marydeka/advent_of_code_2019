#read from input to get instructions for both wires
with open('input.txt') as f:
    lines = f.readlines()

# print(len(lines))

wire1_instructions = lines[0].strip().split(',')
# print(wire1_instructions[0])

wire2_instructions = lines[1].strip().split(',')
# print(wire2_instructions)


#set x and y coordinates for each wire to be 0,0
wire1 = [0,0]
# print("wire1 0th element equals: " + str(wire1[0]))
wire2 = [0,0]

#create a dictionary with all of the points (x, y coordinates) that wire1 passes through
#and the length of the wire up to that point
wire1_path = {}

#create a list with all of the points (x, y coordinates) that wire2 passes through
#and the length of the wire up to that point

wire2_path = {}

wire1_length = 0
wire2_length = 0

# wire1_instructions = ["R10", "L5", "U7", "D2"]
print(wire1_instructions)
for i in range(len(wire1_instructions)):
    instruction = wire1_instructions[i]
    letter = instruction[0]
    movement = int(instruction[1:])
    if letter == 'R':
        for j in range(movement):
            wire1[0] += 1
            wire1_length += 1
            point = "{}:{}".format(wire1[0], wire1[1])
            #the dictionary only contains the length of wire the first time it got to that point
            if point not in wire1_path:
                wire1_path[point] = wire1_length
    elif letter == 'L':
        for j in range(movement):
            wire1[0] -= 1
            wire1_length += 1
            point = "{}:{}".format(wire1[0], wire1[1])
            #the dictionary only contains the length of wire the first time it got to that point
            if point not in wire1_path:
                wire1_path[point] = wire1_length
    elif letter == 'U':
        for j in range(movement):
            wire1[1] += 1
            wire1_length += 1
            point = "{}:{}".format(wire1[0], wire1[1])
            #the dictionary only contains the length of wire the first time it got to that point
            if point not in wire1_path:
                wire1_path[point] = wire1_length
    elif letter == 'D':
        for j in range(movement):
            wire1[1] -= 1
            wire1_length += 1
            point = "{}:{}".format(wire1[0], wire1[1])
            #the dictionary only contains the length of wire the first time it got to that point
            if point not in wire1_path:
                wire1_path[point] = wire1_length
    else:
        print("incorrect instruction letter")
       
print(len(wire1_path))

for i in range(len(wire2_instructions)):
    instruction = wire2_instructions[i]
    letter = instruction[0]
    movement = int(instruction[1:])
    if letter == 'R':
        for j in range(movement):
            wire2[0] += 1
            wire2_length += 1
            point = "{}:{}".format(wire2[0], wire2[1])
            #the dictionary only contains the length of wire the first time it got to that point
            if point not in wire2_path:
                wire2_path[point] = wire2_length
    elif letter == 'L':
        for j in range(movement):
            wire2[0] -= 1
            wire2_length += 1
            point = "{}:{}".format(wire2[0], wire2[1])
            #the dictionary only contains the length of wire the first time it got to that point
            if point not in wire2_path:
                wire2_path[point] = wire2_length
    elif letter == 'U':
        for j in range(movement):
            wire2[1] += 1
            wire2_length += 1
            point = "{}:{}".format(wire2[0], wire2[1])
            #the dictionary only contains the length of wire the first time it got to that point
            if point not in wire2_path:
                wire2_path[point] = wire2_length
    elif letter == 'D':
        for j in range(movement):
            wire2[1] -= 1
            wire2_length += 1
            point = "{}:{}".format(wire2[0], wire2[1])
            #the dictionary only contains the length of wire the first time it got to that point
            if point not in wire2_path:
                wire2_path[point] = wire2_length
    else:
        print("incorrect instruction letter")
       
print(len(wire2_path))


#check for any points that are the same in both lists and add them to a list called intersections
intersections = [num for num in wire2_path if num in wire1_path]
print("intersections length: {}".format(len(intersections)))

#for each intersection, calculate total length of both wires (number of steps/points each have crossed)
combined_steps = [wire1_path[num] + wire2_path[num] for num in intersections]


#once there are no more steps to take, find the minimum in the array of distances and that is the answer
print(min(combined_steps))