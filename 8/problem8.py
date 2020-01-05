filename = 'input.txt'

with open(filename) as f:
    lines = f.readlines()

pixels = lines[0].strip()

pixels = list(pixels)
# print(len(pixels))

# print(pixels)

pixel_width = 25
pixel_depth = 6

layers = []

index = 0
layer_length = pixel_width * pixel_depth

# while index < 50:
while index < len(pixels):
    # print("index: {}".format(index))
    layer = []
    for i in range(index, index + layer_length):
        layer.append(pixels[i])
        index += 1
    layers.append(layer)

# print("first layer: {}".format(layers[0]))
# print("second layer: {}".format(layers[1]))

# print(len(layers))

zero_counts = {}

for layer in layers:
    zero_counts[layer.count('0')] = layer

fewest_zeroes_count = None

for count in zero_counts.keys():
    if fewest_zeroes_count == None:
        fewest_zeroes_count = count 
    elif count < fewest_zeroes_count:
        fewest_zeroes_count = count

fewest_zeroes_layer = zero_counts[fewest_zeroes_count]

# print(fewest_zeroes_layer)

one_digits = fewest_zeroes_layer.count('1')

two_digits = fewest_zeroes_layer.count('2')

answer = int(one_digits) * int(two_digits)

print(answer)





