"""
Hamming Distance
Hamming distance is the number of characters that differ between two strings.

To illustrate:

String1: "abcbba"
String2: "abcbda"

Hamming Distance: 1 - "b" vs. "d" is the only difference.
Create a function that computes the hamming distance between two strings.

Examples
hamming_distance("abcde", "bcdef") ➞ 5

hamming_distance("abcde", "abcde") ➞ 0

hamming_distance("strong", "strung") ➞ 1
Notes
Both strings will have the same length.
"""

from edabit.Test import Test


def hamming_distance(txt1, txt2):
    diff = 0
    for ch1, ch2 in zip(txt1, txt2):
        if ch1 != ch2:
            diff += 1
    return diff


if __name__ == '__main__':
    Test.assert_equals(hamming_distance("abcde", "bcdef"), 5)
    Test.assert_equals(hamming_distance("abcde", "abcde"), 0)
    Test.assert_equals(hamming_distance("strong", "strung"), 1)

#     """zip(*iterables, strict=False)
# Iterate over several iterables in parallel, producing tuples with an item from each one.
#
# Example:
#
# >>>
# >>> for item in zip([1, 2, 3], ['sugar', 'spice', 'everything nice']):
# ...     print(item)
# ...
# (1, 'sugar')
# (2, 'spice')
# (3, 'everything nice')
# More formally: zip() returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument iterables.
# """
