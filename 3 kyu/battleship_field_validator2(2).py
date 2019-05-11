from collections import namedtuple
from functools import reduce
from datetime import datetime
import copy


def permutations(l, size):
    result = [[]]
    size_list = len(l)
    for i in [l.copy()] * size:
        result_ = []
        len_result = len(result)
        for i in range(len(result) * len(i)):
            result_.append(result[i % len_result].copy())
        del result
        result = result_

        for index, j in enumerate(result):
            result[index].append(l[int(index / len_result)])
    return list(set([tuple(sorted(i)) for i in result]))


def is_cross(l):
    sum_el = sum([len(i) for i in l])
    sum_unique = len(set(reduce(lambda x, y: x + y, [list(i) for i in l])))
    return sum_el == sum_unique


def validate_battlefield(bf, ships=None):
    if ships is None:
        ships = [(4, 1), (3, 2), (2, 3), (1, 4)]
        if sum([sum(i) for i in bf]) != sum([i[0]*i[1] for i in ships]):
            return False

    if all([i[1] == 0 for i in ships]):
        return True

    if ships == [(4, 0), (3, 0), (2, 0), (1, 4)]:
        return True

    index = [i for i, el in enumerate(ships) if el[1] != 0][0]
    size, count = ships[index][0], ships[index][1]
    options = []
    for x, line in enumerate(bf):
        for y, i in enumerate(line):
            if i == 1:
                coll = bf[x][y:y+size]
                if coll == [1]*size:
                    options.append(tuple((x, y+i) for i in range(size)))
                row = [i[y] for i in bf[x:x+size]]
                if row == [1]*size:
                    options.append(tuple((x+i, y) for i in range(size)))

    if len(options) < count:
        return False
    else:
        for i in filter(is_cross, permutations(options, count)):
            bf_ = [l.copy() for l in bf]
            for j in i:
                for k in j:
                    bf_[k[0]][k[1]] = 0
            ships_ = ships.copy()
            ships_[index] = (size, 0)
            if validate_battlefield(bf_, ships_):
                return True
    return False

bf = [
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 1, 1],
    [0, 0, 0, 1, 1, 1, 1, 0, 0, 1],
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
]


if __name__ == '__main__':
    start = datetime.now()
    print(validate_battlefield(bf))
    print(datetime.now() - start)
