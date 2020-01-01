"""Recursive Version"""

def find_fuel(mass):
    # print(mass)
    fuel_needed = mass // 3 - 2

    #recursively calculate fuel for each mass
    if fuel_needed <= 0:
        return 0
    else:     
        return fuel_needed + find_fuel(fuel_needed)

with open("input.txt") as f:
    lines = f.readlines()   #creates a list with all the lines

masses = [int(line) for line in lines]
# find_fuel(masses[0])
fuel_per_mass = [find_fuel(mass) for mass in masses]

#add together all the recursive totals

total_fuel_needed = sum(fuel_per_mass)

print(total_fuel_needed)



"""Iterative Version"""

total_fuel_needed = 0

filename = 'input.txt'

with open(filename) as f:
    for mass in f:
        # print(mass)
        fuel_needed = 0
        remaining_mass = int(mass)
        while remaining_mass > 0:
            remaining_mass = remaining_mass // 3 - 2
            if remaining_mass > 0:
                fuel_needed += remaining_mass 
        # print(fuel_needed)

        total_fuel_needed += fuel_needed


print("total fuel needed equals: " + str(total_fuel_needed))





