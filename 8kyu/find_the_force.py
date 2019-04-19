def solution(arr_val, arr_unit):
    units = {
        'm': 1, 'cm': 0.01, 'mm': 0.001, 'μm': 0.000001, 'ft': 0.3048,
        "kg": 1, "g": 0.001, "mg": 0.000001, "μg": 1e-09, "lb": 0.453592
    }

    arr_val = [arr_val[i] * units[arr_unit[i]] for i in range(3)]
    return 6.67e-11 * ((arr_val[0] * arr_val[1]) / (arr_val[2]**2))


if __name__ == "__main__":
    print(solution([1000, 1000, 100], ["g", "kg", "m"]))
