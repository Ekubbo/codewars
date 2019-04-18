def race(v1, v2, g):
    if v2 - v1 <= 0:
        return None

    sec = int((g / (v2 - v1)) * 3600)
    return sec // 3600, (sec % 3600) // 60, (sec % 3600) % 60


if __name__ == "__main__":
    print(race(80, 91, 37))
    print(race(80, 100, 40))
    print(race(720, 850, 70))
