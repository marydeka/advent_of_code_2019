filename = 'input.txt'

with open(filename) as f:
    lines = f.readlines()

# print(len(lines))
# print(lines[0])

orbits = [line.strip() for line in lines]
# print(orbits)

# orbits = ['6CF)4J7', 'RC4)H87', 'M22)RC4']

count = 0
orbits_dict = {}

# ex = orbits[0]
# print(ex[:3])

#Could also split on the ')' instead of slicing
for orbit in orbits:
    if orbit[4:] not in orbits_dict:
        #child is the one orbiting around the parent
        child = orbit[4:]
        parent = orbit[:3]
        orbits_dict[child] = parent

# print(orbits_dict)

#Ideally come up with more meaningful names
for key in orbits_dict.keys():
    # if orbits_dict[key] != None:
        count += 1
        while key in orbits_dict:
            key = orbits_dict[key]
            if key in orbits_dict:
                count += 1

print(count)