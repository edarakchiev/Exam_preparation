def best_list_pureness(number_list, k):
    counter = 0
    pureness_value = -999999999999
    for i in range(k+1):
        current_nums = []

        for index in range(len(number_list)):
            current_result = number_list[index] * index
            current_nums.append(current_result)

        current_sum = sum(current_nums)
        if current_sum > pureness_value:
            pureness_value = current_sum
            counter = i

        number_list.insert(0, number_list.pop())

    return f"Best pureness {pureness_value} after {counter} rotations"






test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)


