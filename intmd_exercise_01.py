def get_unique_list(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

test_list = [1, 2, 3, 2, 1, 4]
print(get_unique_list(test_list))