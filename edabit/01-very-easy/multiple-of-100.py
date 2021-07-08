"""
Multiple of 100
Create a function that takes an integer and return True if it's divisible by 100, otherwise return False.

Examples
divisible(1) ➞ False

divisible(1000) ➞ True

divisible(100) ➞ True
Notes
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.
"""
from edabit.Test import Test


def divisible(num):
    if num % 100 == 0:
        return True
    else:
        return False



if __name__ == '__main__':
        Test.assert_equals(divisible(1), False)
        Test.assert_equals(divisible(100), True)
        Test.assert_equals(divisible(1000), True)
        Test.assert_equals(divisible(111000), True)
        Test.assert_equals(divisible(-1), False)
        Test.assert_equals(divisible(0), True)
        Test.assert_equals(divisible(-100), True)
