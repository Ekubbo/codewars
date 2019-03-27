# Your task, is to create a NxN spiral with a given size.

# For example, spiral with size 5 should look like this:

# 00000
# ....0
# 000.0
# 0...0
# 00000
# and with the size 10:

# 0000000000
# .........0
# 00000000.0
# 0......0.0
# 0.0000.0.0
# 0.0..0.0.0
# 0.0....0.0
# 0.000000.0
# 0........0
# 0000000000
# Return value should contain array of arrays, of 0 and 1, for example for given size 5 result should be:

# [[1,1,1,1,1],[0,0,0,0,1],[1,1,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# Because of the edge-cases for tiny spirals, the size will be at least 5.

# General rule-of-a-thumb is, that the snake made with '1' cannot touch to itself.


def on_board(m, x, y):
    return 0 <= x < len(m) and 0 <= y < len(m[x])


def is_touch_yourself(m, x, y):
    count = 0
    for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
        if on_board(m, i, j) and m[i][j] == 1:
            count += 1
    return count >= 2


def is_valid_step(m, x, y):
    return on_board(m, x, y) and not is_touch_yourself(m, x, y)


def spiralize(size):
    m = [[0 for _ in range(size)] for _ in range(size)]

    dx, dy = (0, 1)
    x, y = (0, 0)
    while is_valid_step(m, x, y):
        m[x][y] = 1
        if not is_valid_step(m, x + dx, y + dy):
            dx, dy = dy, -dx
        x, y = x + dx, y + dy
    return m