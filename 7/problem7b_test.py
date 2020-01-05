import copy

from amplifier import Amplifier

my_list = [5,6,7,8,9]

permutations = [[]]

for i in my_list:
    new_permutations = []
    for perm in permutations:
        for j in my_list:
            if j in perm:
                continue
            else:
                new_perm = copy.deepcopy(perm)
                new_perm.append(j)
                new_permutations.append(new_perm)
    permutations = new_permutations

print(len(permutations))

#for debugging purposes
# permutations = [[9,7,8,5,6]]

final_outputs = []
print(len(final_outputs))

for perm in permutations:
    amp_a = Amplifier()
    amp_b = Amplifier()
    amp_c = Amplifier()
    amp_d = Amplifier()
    amp_e = Amplifier()

    print(perm)
    E = 0
    count = 0
    while True:
        count += 1
        # print("     count: {}".format(count))
        # print("--count: {}".format(count))
        # print("A:{},{}".format(perm[0], E))
        A = amp_a.run(perm[0], E)
        if A == "Halted":
            break
        # print("B:{},{}".format(perm[1], A))
        B = amp_b.run(perm[1], A)
        # print("C:{},{}".format(perm[2], B))
        C = amp_c.run(perm[2], B)
        # print("D:{},{}".format(perm[3], C))
        D = amp_d.run(perm[3], C)
        # print("E:{},{}".format(perm[4], D))
        E = amp_e.run(perm[4], D)

        # if count == 2:
        #     break
    print(E)
    final_outputs.append(E)
    # break
    

print(max(final_outputs))








    