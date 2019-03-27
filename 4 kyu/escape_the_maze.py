# That's terrible! Some evil korrigans have abducted you during your sleep and threw you into a maze of thorns in the scrubland D:
# But have no worry, as long as you're asleep your mind is floating freely in the sky above your body.

# Seeing the whole maze from above in your sleep, can you remember the list of movements you'll have to do to get out when you awake?

# Input
# You are given the whole maze maze as a 2D grid, more specifically in your language:

# an array of strings

# maze[0][0] is the top left-hand corner

# maze[len(maze) - 1][len(maze[0]) - 1] is the bottom right-hand corner

# Inside this 2D grid:

# ' ' is some walkable space
# '#' is a thorn bush (you can't pass through)
# '^', '<', 'v' or '>' is your sleeping body facing respectively the top, left, bottom or right side of the map.
# Output
# Write the function escape that returns the list/array of moves you need to do relatively to the direction you're facing in order to escape the maze (you won't be able to see the map when you wake up). as an array of the following instructions:

# 'F' move one step forward
# 'L' turn left
# 'R' turn right
# 'B' turn back
# Note: 'L','R', and 'B' ONLY perform a rotation and will not move your body

# If the maze has no exit, return an empty array.

# This is a real maze, there is no "escape" point. Just reach the edge of the map and you're free!
# You don't explicitely HAVE to find the shortest possible route, but you're quite likely to timeout if you don't ;P
# Aside from having no escape route the mazes will all be valid (they all contain one and only one "body" character and no other characters than the body, "#" and " ". Besides, the map will always be rectangular, you don't have to check that either)


def is_in_maze(x, y, maze):
    return x in range(len(maze)) and y in range(len(maze[x]))


def add_step(x, y, maze, step, is_move):
    if is_in_maze(x, y, maze) and maze[x][y] == 0:
        maze[x][y] = step + 1
        is_move = True
    return maze, is_move


def is_find(maze):
    borderline = maze[0] + maze[-1] + [l[0] for l in maze] + [l[-1] for l in maze]
    return any(map(lambda x: x >= 1, borderline))


def wave(maze):
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
    step = 1
    is_move = True

    while not is_find(maze) and is_move:
        is_move = False
        for x in range(len(maze)):
            for y in range(len(maze[x])):
                if maze[x][y] == step:
                    for x_, y_ in directions:
                        maze, is_move = add_step(x + x_, y + y_, maze, step, is_move)
        step += 1

    if not is_find(maze):
        return []

    x, y = get_win_position(maze)
    result_path = [(x, y)]
    while step != 1:
        for x_, y_ in directions:
            if is_in_maze(x + x_, y + y_, maze) and maze[x + x_][y + y_] == step - 1:
                x, y = x + x_, y + y_
                result_path = [(x, y)] + result_path
                break
        step -= 1
    return result_path


def is_borderline(x, y, maze):
    return x == 0 or x == len(maze) - 1 or y == 0 or y == len(maze[x]) - 1


def get_win_position(maze):
    for x in range(len(maze)):
        for y in range(len(maze[x])):
            if maze[x][y] >= 1 and is_borderline(x, y, maze):
                return x, y
    return 0, 0


def convert_maze(maze):
    result = []
    for line in maze:
        line_ = []
        for x in line:
            if x == "#":
                line_.append(-1)
            elif x == " ":
                line_.append(0)
            elif x in "><^v":
                line_.append(1)
        result.append(line_)
    return result


def escape(maze):
    path = wave(convert_maze(maze))

    if path == []:
        return []

    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
    init_directions = maze[path[0][0]][path[0][1]]
    direction = directions[">v<^# ".index(init_directions) % 5]

    result = []
    for i in range(1, len(path)):
        x, y = path[i][0], path[i][1]
        prev_x, prev_y = path[i - 1][0], path[i - 1][1]

        if direction != (x - prev_x, y - prev_y):
            ind = directions.index((x - prev_x, y - prev_y))
            if directions[(ind + 1) % 4] == direction:
                result.append("L")
            elif directions[(ind - 1) % 4] == direction:
                result.append("R")
            else:
                result.append("B")
            direction = (x - prev_x, y - prev_y)
        result.append("F")

    return result
