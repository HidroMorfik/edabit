"""
"""

"""
from edabit.Test import Test

if __name__ == '__main__':


"""
from edabit.Test import Test


def convert(hours, minutes):
    return hours * 3600 + minutes * 60


if __name__ == '__main__':
    Test.assert_equals(convert(1, 0), 3600)
    Test.assert_equals(convert(1, 3), 3780)
    Test.assert_equals(convert(0, 30), 1800)
