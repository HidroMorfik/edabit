"""
Nth Even Number
Create a function that takes a number n and returns the nth even number.

Examples
nth_even(1) ➞ 0
# 0 is first even number

nth_even(2) ➞ 2
# 2 is second even number

nth_even(100) ➞ 198
Notes
N/A
"""
from edabit.Test import Test


def nth_even(n):
    return (n * 2) - 2


if __name__ == '__main__':
    Test.assert_equals(nth_even(1), 0)
    Test.assert_equals(nth_even(2), 2)
    Test.assert_equals(nth_even(3), 4)
    Test.assert_equals(nth_even(100), 198)
    Test.assert_equals(nth_even(1298734), 2597466)
