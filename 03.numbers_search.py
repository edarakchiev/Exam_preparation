def numbers_searching(*args):
    sequence = []
    duplicate = []
    missing = []
    for num in args:
        if num not in sequence:
            sequence.append(num)
        else:
            duplicate.append(num)
    min_num = min(sequence)
    max_num = max(sequence)
    for n in range(min_num, max_num):
        if n not in sequence:
            missing.append(n)
    result = sorted(missing)
    duplicate = list(set(duplicate))
    result.append(sorted([num for num in duplicate]))
    return result


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
