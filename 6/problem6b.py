filename = 'input.txt'

with open(filename) as f:
    lines = f.readlines()

orbits = [line.strip() for line in lines]
# print(orbits)

# orbits = ['6CF)4J7', 'RC4)H87', 'M22)RC4']

count = 0
orbits_dict = {}

visited_nodes = {}

for orbit in orbits:
    if orbit[4:] not in orbits_dict:
        #child is the one orbiting around the parent
        child = orbit[4:]
        parent = orbit[:3]
        orbits_dict[child] = parent

key = 'SAN'
distance = 0

while key in orbits_dict:
    distance += 1
    key = orbits_dict[key]
    visited_nodes[key] = distance

# print(visited_nodes)

key2 = 'YOU'
orbital_transfers = 0

while key2 in orbits_dict:
    count += 1
    key2 = orbits_dict[key2]
    if key2 in orbits_dict:
        if key2 in visited_nodes:
            orbital_transfers = visited_nodes[key2] + count - 2
            print("common ancestor found")
            break
            

print("orbital tranfers: {}".format(orbital_transfers))
