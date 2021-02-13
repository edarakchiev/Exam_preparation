def matrix_init(n):
    m = []
    for _ in range(n):
        current_r = [" "] * n
        m.append(current_r)
    return m


def coordinates_read(num_coord):
    coord = []
    for _ in range(num_coord):
        data_reading = input()
        data = data_reading[1:-1]
        data = data.split(", ")
        current_row = int(data[0])
        current_col = int(data[1])
        coord.append((current_row, current_col))
    return coord


def bombs_put(m, coord):
    for point in coord:
        row = point[0]
        col = point[1]
        m[row][col] = "*"
    return m


def calculate_bombs(m, n):
    for r in range(n):
        for c in range(n):
            if not m[r][c] == "*":
                counter = 0
                if c > 0:
                    if m[r][c - 1] == "*":
                        counter += 1
                if c < n - 1:
                    if m[r][c + 1] == "*":
                        counter += 1
                if r > 0:
                    if m[r - 1][c] == "*":
                        counter += 1
                if r > 0 and c > 0:
                    if m[r - 1][c - 1] == "*":
                        counter += 1
                if r > 0 and c < n - 1:
                    if m[r - 1][c + 1] == "*":
                        counter += 1
                if r < n - 1:
                    if m[r + 1][c] == "*":
                        counter += 1
                if r < n - 1 and c > 0:
                    if m[r + 1][c - 1] == "*":
                        counter += 1
                if r < n - 1 and c < n - 1:
                    if m[r + 1][c + 1] == "*":
                        counter += 1
                m[r][c] = str(counter)
    return m


size = int(input())
matrix = matrix_init(size)
number_coordinates = int(input())
coordinates = coordinates_read(number_coordinates)
matrix = bombs_put(matrix, coordinates)
matrix = calculate_bombs(matrix, size)
[print(*el) for el in matrix]