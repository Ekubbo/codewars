# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

# Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item. It must return the display text as shown in the examples:

# likes [] // must be "no one likes this"
# likes ["Peter"] // must be "Peter likes this"
# likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
# likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
# likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"
# For 4 or more names, the number in and 2 others simply increases.

# https://www.codewars.com/kata/5266876b8f4bf2da9b000362


def likes(names):
    if names == []:
        return 'no one likes this'
    elif len(names) == 1:
        return "{name} likes this".format(name=", ".join(names))
    elif len(names) == 3 or len(names) == 2:
        return "{names} and {name} like this".format(names=", ".join(names[:(2 if len(names) == 3 else 1)]), name=names[-1])
    return "{names} and {count} others like this".format(names=", ".join(names[:(2)]), count=str(len(names) - 2))

