# The main idea is to count all the occuring characters(UTF-8) in string. If you have string like this aba then the result should be { 'a': 2, 'b': 1 }

# What if the string is empty ? Then the result should be empty object literal { }

# For C#: Use a Dictionary<char, int> for this kata!

# https://www.codewars.com/kata/52efefcbcdf57161d4000091


def count(string):
    r = {}
    for s in string:
        if s in r:
            r[s] += 1
        else:
            r[s] = 1
    return r
