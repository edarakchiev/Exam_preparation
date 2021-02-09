def matrix_init(n):
    m = []
    for _ in range(n):
        current_row = [el for el in input()]
        m.append(current_row)
    return m


def check_player_position(m, n):
    for r in range(n):
        for c in range(n):
            if m[r][c] == "P":
                return r, c


text = [ch for ch in input()]
size = int(input())
matrix = matrix_init(size)
commands_number = int(input())
player_row, player_col = check_player_position(matrix, size)

for _ in range(commands_number):
    command = input()
    if command == "up":
        player_row -= 1
        if player_row >= 0:
            if matrix[player_row][player_col].isalpha():
                alpha = matrix[player_row][player_col]
                text.append(alpha)
            matrix[player_row][player_col] = "P"
            matrix[player_row+1][player_col] = "-"
        else:
            text.pop()
            player_row += 1

    elif command == "down":
        player_row += 1
        if player_row < size:
            if matrix[player_row][player_col].isalpha():
                alpha = matrix[player_row][player_col]
                text.append(alpha)
            matrix[player_row][player_col] = "P"
            matrix[player_row-1][player_col] = "-"
        else:
            text.pop()
            player_row -= 1

    elif command == "left":
        player_col -= 1
        if player_col >= 0:
            if matrix[player_row][player_col].isalpha():
                alpha = matrix[player_row][player_col]
                text.append(alpha)
            matrix[player_row][player_col] = "P"
            matrix[player_row][player_col+1] = "-"
        else:
            text.pop()
            player_col += 1

    elif command == "right":
        player_col += 1
        if player_col < size:
            if matrix[player_row][player_col].isalpha():
                alpha = matrix[player_row][player_col]
                text.append(alpha)
            matrix[player_row][player_col] = "P"
            matrix[player_row][player_col-1] = "-"
        else:
            text.pop()
            player_col -= 1

print(''.join(text))
for el in matrix:
    print(''.join(el))