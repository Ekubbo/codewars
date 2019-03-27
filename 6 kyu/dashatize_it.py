# Given a number, return a string with dash'-'marks before and after each odd integer, but do not begin or end the string with a dash mark.

# Ex:

# dashatize(274) -> '2-7-4'
# dashatize(6815) -> '68-1-5'

# https://www.codewars.com/kata/58223370aef9fc03fd000071


def is_even(x):
    return 0 is x % 2


def dashatize(num):
    if num is None:
        return "None"

    num_str = str(abs(num))

    result = "".join([s if is_even(int(s)) else "-{}-".format(s) for s in num_str])

    if result[0] == '-': result = result[1:]
    if result[-1] == '-': result = result[:-1]

    return "".join([s for i, s in enumerate(result) if s != '-' or s == '-' and result[i-1] != '-'])
