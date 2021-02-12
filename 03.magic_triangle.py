def get_magic_triangle(n):
    triangle = []
    for first_two_row in range(2):
        triangle.append([])
        triangle[first_two_row] += [1] * (first_two_row + 1)

    for index in range(2, n):
        triangle.append([])
        for e in range(index + 1):
            if e == 0:
                triangle[index].append(triangle[index - 1][e])
            elif 0 < e < index:
                triangle[index].append(triangle[index - 1][e - 1] + triangle[index-1][e])
            elif e == index:
                triangle[index].append(triangle[index-1][e-1])
    return triangle



print(get_magic_triangle(5))
