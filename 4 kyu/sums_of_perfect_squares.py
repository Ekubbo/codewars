# The task is simply stated. Given an integer n (3 < n < 109), find the length of the smallest list of perfect squares which add up to n. Come up with the best algorithm you can; you'll need it!

# Examples:

# sum_of_squares(17) = 2 
# 17 = 16 + 1 (4 and 1 are perfect squares).
# sum_of_squares(15) = 4 
# 15 = 9 + 4 + 1 + 1. There is no way to represent 15 as the sum of three perfect squares.
# sum_of_squares(16) = 1 
# 16 itself is a perfect square.
# Time constraints:

# 5 easy (sample) test cases: n < 20

# 5 harder test cases: 1000 < n < 15000

# 5 maximally hard test cases: 5 * 1e8 < n < 1e9

# 300 random maximally hard test cases: 1e8 < n < 1e9

# https://www.codewars.com/kata/sums-of-perfect-squares/train/java


def is_square(n):
    return int(n**0.5) ** 2 == n


# def sum_of_squares(n):
#     rs = {}
#     for i in range(n + 1):
#         if is_square(i):
#             rs[i] = 1
#         else:
#             rs[i] = rs[1] + rs[i - 1]
#             for x in range(2, int(i / 2) + 1):
#                 rs[i] = min(rs[x] + rs[i - x], rs[i])
#     return rs[n]


def sum_of_squares(n):
    if is_square(n):
        return 1

    temp = n
    while temp % 4 == 0:
        temp /= 4

    if temp % 8 == 7:
        return 4

    for i in range(int(n**0.5) + 1):
        if is_square(n - i*i):
            return 2
    return 3


if __name__ == "__main__":
    print(sum_of_squares(21))
