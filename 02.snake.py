def matrix_init():
    n = int(input())
    m = []
    for _ in range(n):
        r = [el for el in input()]
        m.append(r)
    return m, n


def check_position(m):
    for r in range(len(m)):
        for c in range(len(m[r])):
            if m[r][c] == "S":
                return r, c


def lair_checker(m):
    lair_coord = []
    for r in range(len(m)):
        for c in range(len(m[r])):
            if m[r][c] == "B":
                lair_coord.append(r)
                lair_coord.append(c)
    return lair_coord


def lair_position(m, curr_row, curr_col):
    r_1, c_1, r_2, c_2 = lair_checker(m)
    if curr_row == r_1 and curr_col == c_1:
        m[r_1][c_1] = "."
        curr_row = r_2
        curr_col = c_2
        return m, curr_row, curr_col
    elif curr_row == r_2 and curr_col == c_2:
        m[r_2][c_2] = "."
        curr_row = r_1
        curr_col = c_1
        return m, curr_row, curr_col


matrix, size = matrix_init()
current_row, current_col = check_position(matrix)
food = 0
while True:
    if food == 10:
        print("You won! You fed the snake.")
        break
    command = input()
    if command == "up":
        matrix[current_row][current_col] = "."
        if current_row > 0:
            current_row -= 1
        else:
            print("Game over!")
            break
        if matrix[current_row][current_col] == "*":
            food += 1
        elif matrix[current_row][current_col] == "B":
            matrix, current_row, current_col = lair_position(matrix, current_row, current_col)

    elif command == "down":
        matrix[current_row][current_col] = "."
        if current_row < size - 1:
            current_row += 1
        else:
            print("Game over!")
            break
        if matrix[current_row][current_col] == "*":
            food += 1
        elif matrix[current_row][current_col] == "B":
            matrix, current_row, current_col = lair_position(matrix, current_row, current_col)

    elif command == "left":
        matrix[current_row][current_col] = "."
        if current_col > 0:
            current_col -= 1
        else:
            print("Game over!")
            break
        if matrix[current_row][current_col] == "*":
            food += 1
        elif matrix[current_row][current_col] == "B":
            matrix, current_row, current_col = lair_position(matrix, current_row, current_col)

    elif command == "right":
        matrix[current_row][current_col] = "."
        if current_col < size - 1:
            current_col += 1
        else:
            print("Game over!")
            break
        if matrix[current_row][current_col] == "*":
            food += 1
        elif matrix[current_row][current_col] == "B":
            matrix, current_row, current_col = lair_position(matrix, current_row, current_col)
    matrix[current_row][current_col] = "S"

print(f"Food eaten: {food}")
[print(''.join(el)) for el in matrix]
