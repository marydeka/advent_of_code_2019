num_valid_passwords = 0

# for num in range(1200,1234):
for num in range(372304, 847060):
    string_num = str(num)
    char_arr = list(string_num)

    double_num = False

    for i in range(len(char_arr) - 1):
        if char_arr[i] == char_arr[i + 1]:
            double_num = True

    # print("{}: {}".format(num, double_num))

    increasing = True

    # if double_num == True:

    for i in range(len(char_arr) - 1):
        if int(char_arr[i]) > int(char_arr[i + 1]): 
            # print("{} <= {}".format(char_arr[i], char_arr[i + 1]))
            increasing = False
            break

    # if increasing == True:
    print("{}:{}: {}".format(num, double_num, increasing))
    
    if double_num and increasing:
        num_valid_passwords += 1

print(num_valid_passwords)

