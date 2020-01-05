filename = 'input.txt'

with open(filename) as f:
    lines = f.readlines()

pixels = lines[0].strip()

pixels = list(pixels)
# pixels = ['0','2','2','2','1','1','2','2','2','2','1','2','0','0','0','0']

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

final_colors = []

j = 0
while j < (pixel_width * pixel_depth):
    color = '2'
    for layer in layers:
        if layer[j] == '1':
            color = '1'
            break
        elif layer[j] == '0':
            color = ' '
            break
    final_colors.append(color)
    j += 1
    
# print(final_colors)

k = 0
while k < pixel_width * pixel_depth:
    # print("k: {}".format(k))
    print(''.join(final_colors[k: k + pixel_width]))
    k += pixel_width
    









