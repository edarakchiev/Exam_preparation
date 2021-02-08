def matrix_init():
    m = []
    for _ in range(size):
        current_row = [el for el in input().split()]
        m.append(current_row)
    return m


size = 8

matrix = matrix_init()
king_row = 0
king_col = 0
for row in range(size):
    for col in range(size):
        if matrix[row][col] == "K":
            king_row = row
            king_col = col

coordinates = []

for r in range(king_row - 1, -1, -1):  # UP
    if matrix[r][king_col] == "Q":
        result = [r, king_col]
        coordinates.append(result)
        r = 0
        break

for r in range(king_row + 1, size):  # DOWN
    if matrix[r][king_col] == "Q":
        result = [r, king_col]
        coordinates.append(result)
        r = 0
        break

for c in range(king_col + 1, size):  # RIGHT
    if matrix[king_row][c] == "Q":
        result = [king_row, c]
        coordinates.append(result)
        c = 0
        break

for c in range(king_col - 1, -1, -1):  # LEFT
    if matrix[king_row][c] == "Q":
        result = [king_row, c]
        coordinates.append(result)
        c = 0
        break

c = king_col
for r in range(king_row - 1, -1, -1):  # UP_RIGHT
    c += 1
    if c == size:
        break
    if matrix[r][c] == "Q":
        result = [r, c]
        coordinates.append(result)
        break

c = 0
c = king_col
for r in range(king_row - 1, -1, -1):  # UP_LEFT
    c -= 1
    if c < 0:
        break
    if matrix[r][c] == "Q":
        result = [r, c]
        coordinates.append(result)
        break

r = 0
c = king_col
for r in range(king_row + 1, size):  # DOWN_RIGHT
    c += 1
    if c == size:
        break
    if matrix[r][c] == "Q":
        result = [r, c]
        coordinates.append(result)
        break
r = 0
c = king_col

for r in range(king_row + 1, size):  # DOWN_LEFT
    c -= 1
    if c < 0:
        break
    elif matrix[r][c] == "Q":
        result = [r, c]
        coordinates.append(result)
        break
if coordinates:
    [print(coordinate) for coordinate in coordinates]
else:
    print("The king is safe!")