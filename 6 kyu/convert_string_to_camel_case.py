# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized.

# Examples
# to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"

# to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"

# https://www.codewars.com/kata/517abf86da9663f1d2000003


import re


def upperWord(word):
    if len(word) > 0:
        word = list(word)
        word[0] = word[0].upper()
    return "".join(word)


def to_camel_case(text):
    text = re.split("_", re.sub('-', '_', text))
    text = list(text[0]) + list(map(upperWord, text[1:]))
    return "".join(text)
