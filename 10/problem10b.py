import sys
import math

filename = 'input.txt'
# filename = 'input2.txt'

with open(filename) as f:
    lines = f.readlines()

space_area = lines

width = len(lines[0].strip())
depth = len(lines)

def calc_signature(x1,x2,y1,y2):
    if (y2 - y1) == 0:
        signature = sys.maxsize
    else:
        signature = (x2 - x1)/(y2 - y1)
    x_quad = 1 if x1 > x2 else 0
    y_quad = 1 if y1 > y2 else 0
    return "{}:{}:{}".format(signature, x_quad, y_quad)

asteroid_map = {}

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
    # print("entered loop")
    print("count: {}".format(asteroid_map[monitoring_station]))
    if asteroid_map[monitoring_station] > max_count:
        max_count = asteroid_map[monitoring_station]
        best_monitoring_station = monitoring_station

def calc_angle(y,x):
    if best_monitoring_station is not None:
        y1 = best_monitoring_station[1]
        x1 = best_monitoring_station[0]
        angle = math.atan2(y - y1,x - x1) * (180 / math.pi) + 90
        return angle

for x in range(width):
    for y in range(depth):
        # print("({}, {})".format(x,y))
        if space_area[y][x] == '#':
            asteroid_map[(x, y)] = calc_angle(y,x)

print("monitoring station: {}".format(best_monitoring_station))




for asteroid in asteroid_map.keys():
    x2 = asteroid[0]
    y2 = asteroid[1]

asteroid_angles = {}

for asteroid, angle in asteroid_map.items():
    if angle not in asteroid_angles:
        asteroid_angles[angle] = [asteroid]
    else:
        asteroid_angles[angle].append(asteroid)

# print("asteroid map: {}".format(asteroid_map))

# print("asteroid angles: {}".format(asteroid_angles))

all_angles = [key for key in asteroid_angles.keys()]

print(sorted(all_angles))