# In this kata you have to create all permutations of an input string and remove duplicates, if present. This means, you have to shuffle all letters from the input in all possible orders.

# Examples:

# permutations('a'); # ['a']
# permutations('ab'); # ['ab', 'ba']
# permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
# The order of the permutations doesn't matter.

# https://www.codewars.com/kata/5254ca2719453dcc0b00027d


def permutations(string):
    if len(string) == 1: return [string]

    result = []
    for i, x in enumerate(string):
        result += [x + word for word in permutations(string[:i] + string[i + 1:])]
    return list(set(result))
