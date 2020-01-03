num_valid_passwords = 0

# for num in range(1200,1800):
for num in range(372304, 847060):
    string_num = str(num)
    char_arr = list(string_num)

    double_num = False

    if char_arr[len(char_arr) - 2] == char_arr[len(char_arr) - 1] and char_arr[len(char_arr) - 2] != char_arr[len(char_arr) - 3]:
        double_num = True

    if char_arr[0] == char_arr[1] and char_arr[1] != char_arr[2]:
        double_num = True

    if double_num == False:
        for i in range(1, len(char_arr) - 2):
            if char_arr[i] == char_arr[i + 1] and char_arr[i + 1] != char_arr[i + 2] and char_arr[i] != char_arr[i - 1]:
                double_num = True
                break

    # print("{}: {}".format(num, double_num))

    increasing = True

    # if double_num == True:

    for i in range(len(char_arr) - 1):
        if int(char_arr[i]) > int(char_arr[i + 1]): 
            # print("{} <= {}".format(char_arr[i], char_arr[i + 1]))
            increasing = False
            break

    # if increasing == True:
    # print("{}:{}: {}".format(num, double_num, increasing))
    
    if double_num and increasing:
        print("{}:{}: {}".format(num, double_num, increasing))
        num_valid_passwords += 1

print(num_valid_passwords)

