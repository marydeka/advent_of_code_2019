import sys

filename = 'input.txt'
# filename = 'input2.txt'

with open(filename) as f:
    lines = f.readlines()

space_area = lines

width = len(lines[0].strip())
depth = len(lines)

# print(width)
# print(depth)

def calc_signature(x1,x2,y1,y2):
    if (y2 - y1) == 0:
        signature = sys.maxsize
    else:
        signature = (x2 - x1)/(y2 - y1)
    x_quad = 1 if x1 > x2 else 0
    y_quad = 1 if y1 > y2 else 0
    return "{}:{}:{}".format(signature, x_quad, y_quad)

asteroid_map = {}

for x in range(width):
    for y in range(depth):
        # print("({}, {})".format(x,y))
        if space_area[y][x] == '#':
            asteroid_map[(x, y)] = 0

for asteroid in asteroid_map.keys():
    x2 = asteroid[0]
    y2 = asteroid[1]

    count = 0

    unique_angles = {}

    for other_asteroid in asteroid_map.keys():
        if other_asteroid == asteroid:
            continue
        else:
            x1 = other_asteroid[0]
            y1 = other_asteroid[1]
            signature = calc_signature(x1,x2,y1,y2)
            # print("     {}:{}".format(other_asteroid, signature))
            # break
            if signature not in unique_angles:
                count += 1
                unique_angles[signature] = 0
                

    asteroid_map[asteroid] = count
    # print("count: {}".format(count))
    

# print(asteroid_map)

max_count = 0
best_monitoring_station = None

for monitoring_station in asteroid_map.keys():
    if asteroid_map[monitoring_station] > max_count:
        max_count = asteroid_map[monitoring_station]
        best_monitoring_station = monitoring_station

most_asteroids_monitored = asteroid_map[best_monitoring_station]

print("asteroids located at these points: {}".format(asteroid_map))

print(best_monitoring_station)
print(most_asteroids_monitored)

# print(asteroid_map)
