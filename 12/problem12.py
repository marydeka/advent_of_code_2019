import re
import math

filename = 'input.txt'

with open(filename) as f:
    lines = f.readlines()

lines = [line.strip().split(',') for line in lines]

for i in range(len(lines)):
    lines[i] = "".join(lines[i])

num_moons = len(lines)
time_steps = 1000

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

for step in range(time_steps):
    update_velocity()
    update_position()
   

def find_total_energy():
    pos_positions = positions.copy()
    pos_velocities = velocities.copy()
    for i in range(num_moons):
        pos_positions[i] = [abs(num) for num in positions[i]]
        pos_velocities[i] = [abs(num) for num in velocities[i]]

    #create a list of total potential energies and a list of total kinetic energies for each moon
    moon_potential_energies = [sum(moon) for moon in pos_positions]
    moon_kinetic_energies = [sum(moon) for moon in pos_velocities]

    total_energy = 0
    for i in range(len(moon_potential_energies)):
        total_energy += moon_potential_energies[i] * moon_kinetic_energies[i]
        print(total_energy)
    return total_energy

print(find_total_energy())

