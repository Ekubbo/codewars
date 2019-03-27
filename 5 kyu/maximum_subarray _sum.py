# The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

# maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]
# Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

# Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.

#  https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c


def maxSequence(arr):
    result = 0
    for i, j in [[i1, i2] for i1 in range(len(arr) + 1) for i2 in range(len(arr) + 1)]:
        result = max(result, sum(arr[i:j]))
    return result