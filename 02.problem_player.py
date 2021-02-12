def matrix_init(num):
    m = []
    for _ in range(num):
        current_r = [el for el in input()]
        m.append(current_r)
    return m


def player_position(m, num):
    for r in range(num):
        for c in range(num):
            if m[r][c] == "P":
                return r, c


text = input()
n = int(input())
matrix = matrix_init(n)
command_number = int(input())
current_row, current_col = player_position(matrix, n)

for _ in range(command_number):
    command = input()
    if command == "up":

        if current_row > 0:
            current_row -= 1
            if matrix[current_row][current_col].isalpha():
                text += matrix[current_row][current_col]
            matrix[current_row + 1][current_col] = "-"
        else:
            text = text[:-1]

    elif command == "down":

        if current_row < n - 1:
            current_row += 1
            if matrix[current_row][current_col].isalpha():
                text += matrix[current_row][current_col]
            matrix[current_row - 1][current_col] = "-"
        else:
            text = text[:-1]

    elif command == "left":
        if current_col > 0:
            current_col -= 1
            if matrix[current_row][current_col].isalpha():
                text += matrix[current_row][current_col]
            matrix[current_row][current_col + 1] = "-"
        else:
            text = text[:-1]

    elif command == "right":

        if current_col < n - 1:
            current_col += 1
            if matrix[current_row][current_col].isalpha():
                text += matrix[current_row][current_col]
            matrix[current_row][current_col - 1] = "-"
        else:
            text = text[:-1]
    matrix[current_row][current_col] = "P"

print(''.join(text))
for row in matrix:
    print("".join(row))
