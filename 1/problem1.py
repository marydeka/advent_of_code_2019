import math

total_sum = 0

filename = 'input.txt'

with open(filename) as f:
    for line in f:
        line = (math.floor(int(line) / 3)) - 2
        total_sum += line

print("total sum equals: " + str(total_sum))


f.close()
