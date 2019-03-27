# Implement String#ipv4_address?, which should return true if given object is an IPv4 address - four numbers (0-255) separated by dots.

# It should only accept addresses in canonical representation, so no leading 0s, spaces etc.


import re


def ipv4_address(address):
    if re.fullmatch(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', address):
        return all(map(lambda n: 0 <= int(n) <= 255 and (n[0] != "0" or len(n) == 1), address.split(".")))

    return False
