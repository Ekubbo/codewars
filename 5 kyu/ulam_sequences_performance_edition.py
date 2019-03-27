# This is the performance edition of this kata. If you didn't do it yet, you should begin there.

# The Ulam sequence U is defined by u0=u, u1=v, with the general term u_n for n>2 given by the least integer expressible uniquely as the sum of two distinct earlier terms.
# In other words, the next number is always the smallest, unique sum of any two previous terms.

# The first 10 terms of the sequence U(u0=1, u1=2) are [1, 2, 3, 4, 6, 8, 11, 13, 16, 18].

# Here, the first term after the initial 1, 2 is obviously 3 since 3=1+2.
# The next term is 4=1+3 (we don't have to worry about 4=2+2 since it is a sum of a single term instead of two distinct terms)
# 5 is not a member of the sequence since it is representable in two ways: 5=1+4=2+3, but 6=2+4 is a member (since 3+3 isn't a valid calculation).
# You'll have to write a code that creates an Ulam Sequence starting with u0, u1 and containing n terms.

# The pitfall...
# While the passing solutions of the first version could have a time complexity of O(N3) (or even O(N4)!!), with 20 tests up to 100 terms only, here you'll have to manage generation of sequences up to 1500 terms before time out.

# Configuration of the tests:

# 6 small fixed tests
# 20 random tests on small sequences (10 to 30 terms)
# 16 large random tests (1500 terms)
# Inputs:

# u0 and u1: integers, greater than or equal to 1
# n: integer greater than 1, length of the returned list

# https://www.codewars.com/kata/5ac94db76bde60383d000038


def ulam_sequence(u0, u1, n):
    print(u0, u1, n)

    result = [u0, u1]
    s = {u0 + u1}
    s_all = {u0 + u1, u0, u1}
    for _ in range(n - 2):
        x = min(s)
        new = {num + x for num in result}
        s = (s - (new & s_all)) ^ (new - s_all)
        s_all |= new
        s.remove(x)
        result.append(x)
    return result
