"""
Find ASCII Charcode of Inverse Case Character
Create a function that takes a single character as an argument and returns the char code of its lowercased / uppercased counterpart.

Examples
Given that:
  - "A" char code is: 65
  - "a" char code is: 97

counterpartCharCode("A") ➞ 97

counterpartCharCode("a") ➞ 65
Notes
The argument will always be a single character.
Not all inputs will have a counterpart (e.g. numbers), in which case return the inputs char code.

"""

from edabit.Test import Test


def counterpartCharCode(char):
    code = ord(char.swapcase())
    return code


if __name__ == '__main__':
    Test.assert_equals(counterpartCharCode('a'), 65)
    Test.assert_equals(counterpartCharCode('A'), 97)
    Test.assert_equals(counterpartCharCode('l'), 76)
    Test.assert_equals(counterpartCharCode('L'), 108)
    Test.assert_equals(counterpartCharCode('z'), 90)
    Test.assert_equals(counterpartCharCode('Z'), 122)
