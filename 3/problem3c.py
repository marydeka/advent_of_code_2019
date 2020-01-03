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

#create a list with all of the points (x, y coordinates) that wire1 passes through
wire1_path = []

#create a list with all of the points (x, y coordinates) that wire2 passes through
wire2_path = []

# wire1_instructions = ["R10", "L5", "U7", "D2"]
print(wire1_instructions)
for i in range(len(wire1_instructions)):
    instruction = wire1_instructions[i]
    letter = instruction[0]
    movement = int(instruction[1:])
    if letter == 'R':
        for j in range(movement):
            wire1[0] += 1
            wire1_path.append("{}:{}".format(wire1[0], wire1[1]))
    elif letter == 'L':
        for j in range(movement):
            wire1[0] -= 1
            wire1_path.append("{}:{}".format(wire1[0], wire1[1]))
    elif letter == 'U':
        for j in range(movement):
            wire1[1] += 1
            wire1_path.append("{}:{}".format(wire1[0], wire1[1]))
    elif letter == 'D':
        for j in range(movement):
            wire1[1] -= 1
            wire1_path.append("{}:{}".format(wire1[0], wire1[1]))
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
            wire2_path.append("{}:{}".format(wire2[0], wire2[1]))
    elif letter == 'L':
        for j in range(movement):
            wire2[0] -= 1
            wire2_path.append("{}:{}".format(wire2[0], wire2[1]))
    elif letter == 'U':
        for j in range(movement):
            wire2[1] += 1
            wire2_path.append("{}:{}".format(wire2[0], wire2[1]))
    elif letter == 'D':
        for j in range(movement):
            wire2[1] -= 1
            wire2_path.append("{}:{}".format(wire2[0], wire2[1]))
    else:
        print("incorrect instruction letter")
       
print(len(wire2_path))


#check for any points that are the same in both lists and add them to a list called intersections
intersections = [num for num in wire2_path if num in wire1_path]
print("intersections length: {}".format(len(intersections)))

#for each intersection, calculate the number of steps (number of points) 
#that the two wires have taken to get to that intersection
distances = [wire1_path.index(point) + wire2_path.index(point) + 2 for point in intersections ]


#once there are no more steps to take, find the minimum in the array of distances and that is the answer
print(min(distances))