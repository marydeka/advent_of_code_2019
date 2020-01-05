import copy

my_list = [0,1,2,3,4]

permutations = [[]]

for i in my_list:
    new_permutations = []
    # new_list = [i]
    # permutations.append(new_list)
    for perm in permutations:
        for j in my_list:
            if j in perm:
                continue
            else:
                new_perm = copy.deepcopy(perm)
                new_perm.append(j)
                new_permutations.append(new_perm)
    permutations = new_permutations

print(new_permutations)
print(len(new_permutations))
