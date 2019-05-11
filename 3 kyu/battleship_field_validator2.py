from collections import namedtuple
import copy


def find(m, e):
    for index, line in enumerate(m):
        if e in line:
            element = namedtuple('element', 'x y')
            return element(x=index, y=line.index(e))
    return None


def validate_battlefield(bf, ships=None):
    if ships is None:
        ships = [(4, 1), (3, 2), (2, 3), (1, 4)]
        if sum([sum(i) for i in bf]) != sum([i[0]*i[1] for i in ships]):
            return False

    el = find(bf, 1)
    if all([i[1] == 0 for i in ships]) and el is None:
        return True
    elif el is None:
        return False

    for index, i in enumerate(ships):
        if i[1] == 0:
            continue

        coll = bf[el.x][el.y:el.y+i[0]]
        if coll == [1]*i[0]:
            bf_ = [l[:el.y] + [0]*i[0] + l[el.y+i[0]:] if index == el.x else l.copy() for index, l in enumerate(bf)]
            ships_ = ships.copy()
            ships_[index] = [ships_[index][0], ships_[index][1] - 1]
            if validate_battlefield(bf_, ships_):
                return True

        row = [i[el.y] for i in bf[el.x:el.x+i[0]]]
        if row == [1]*i[0]:
            bf_ = [l[:el.y] + [0] + l[el.y+1:] if index in range(el.x, el.x+i[0]+1) else l.copy() for index, l in enumerate(bf)]
            ships_ = ships.copy()
            ships_[index] = [ships_[index][0], ships_[index][1] - 1]
            if validate_battlefield(bf_, ships_):
                return True

    return False


m = [
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

if __name__ == '__main__':
    print(validate_battlefield(m))