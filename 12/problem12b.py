import re
import math

filename = 'input.txt'

with open(filename) as f:
    lines = f.readlines()

lines = [line.strip().split(',') for line in lines]

for i in range(len(lines)):
    lines[i] = "".join(lines[i])

num_moons = len(lines)
time_steps = 0

#x,y, and z coordinates for positions of all moons
moon_a_pos = [int(d) for d in re.findall(r'-?\d+', lines[0])]
moon_b_pos = [int(d) for d in re.findall(r'-?\d+', lines[1])]
moon_c_pos = [int(d) for d in re.findall(r'-?\d+', lines[2])]
moon_d_pos = [int(d) for d in re.findall(r'-?\d+', lines[3])]

positions = [moon_a_pos] + [moon_b_pos] + [moon_c_pos] + [moon_d_pos]


#x, y, and z coordinates for velocities of all moons
moon_a_vel = [0] * 3
moon_b_vel = [0] * 3
moon_c_vel = [0] * 3
moon_d_vel = [0] * 3

velocities = [moon_a_vel] + [moon_b_vel] + [moon_c_vel] + [moon_d_vel]


def update_velocity():
    #c stands for coordiinate (x, y, or z in this case)
    for c in range(3):
        for i in range(3):
            for j in range(i + 1, num_moons):
                if positions[i][c] < positions[j][c]:
                    velocities[i][c] += 1
                    velocities[j][c] -= 1
                elif positions[i][c] > positions[j][c]:
                    velocities[i][c] -= 1
                    velocities[j][c] += 1

def update_position():
    for i in range(num_moons):
        #c stands for coordinates (x, y, or z in this case)
        for c in range(3):
            positions[i][c] += velocities[i][c]

my_dict = {}

my_dict[str(positions + velocities)] = 0
print(my_dict)

while True:
    update_velocity()
    update_position()
    time_steps += 1
    signature = str(positions + velocities)
    if signature in my_dict:
        print("steps needed to find exact match: {}".format(time_steps))
        break

    my_dict[signature] = time_steps
    # print(my_dict)
   
   
