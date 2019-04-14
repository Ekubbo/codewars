def last_digit(powers):
    last = 1

    for num in reversed(powers):
        last = 1 if last == 0 else num if last == 1 else num**(last % 4 + 4)
    return last % 10


if __name__ == "__main__":
    powers = [3, 9, 7, 1]
    print(last_digit(powers))
