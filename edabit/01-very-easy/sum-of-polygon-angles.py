"""
Sum of Polygon Angles
Given an n-sided regular polygon n, return the total sum of internal angles (in degrees).

Examples
sum_polygon(3) ➞ 180

sum_polygon(4) ➞ 360

sum_polygon(6) ➞ 720
Notes
n will always be greater than 2.
The formula (n - 2) x 180 gives the sum of all the measures of the angles of an n-sided polygon.
"""
from edabit.Test import Test


def sum_polygon(n):
    return (n - 2) * 180


if __name__ == '__main__':
    from time import perf_counter

    tic = perf_counter()
    Test.assert_equals(sum_polygon(3), 180)
    Test.assert_equals(sum_polygon(4), 360)
    Test.assert_equals(sum_polygon(5), 540)
    Test.assert_equals(sum_polygon(6), 720)
    Test.assert_equals(sum_polygon(7), 900)
    Test.assert_equals(sum_polygon(8), 1080)
    Test.assert_equals(sum_polygon(9), 1260)
    Test.assert_equals(sum_polygon(10), 1440)
    Test.assert_equals(sum_polygon(11), 1620)
    Test.assert_equals(sum_polygon(12), 1800)
    Test.assert_equals(sum_polygon(13), 1980)
    Test.assert_equals(sum_polygon(14), 2160)
    Test.assert_equals(sum_polygon(15), 2340)
    Test.assert_equals(sum_polygon(16), 2520)
    Test.assert_equals(sum_polygon(17), 2700)
    Test.assert_equals(sum_polygon(18), 2880)
    Test.assert_equals(sum_polygon(19), 3060)
    Test.assert_equals(sum_polygon(20), 3240)
    Test.assert_equals(sum_polygon(21), 3420)
    Test.assert_equals(sum_polygon(22), 3600)
    Test.assert_equals(sum_polygon(23), 3780)
    Test.assert_equals(sum_polygon(24), 3960)
    Test.assert_equals(sum_polygon(25), 4140)
    Test.assert_equals(sum_polygon(26), 4320)
    Test.assert_equals(sum_polygon(27), 4500)
    Test.assert_equals(sum_polygon(28), 4680)
    Test.assert_equals(sum_polygon(29), 4860)
    Test.assert_equals(sum_polygon(30), 5040)
    Test.assert_equals(sum_polygon(31), 5220)
    Test.assert_equals(sum_polygon(32), 5400)
    Test.assert_equals(sum_polygon(33), 5580)
    Test.assert_equals(sum_polygon(34), 5760)
    Test.assert_equals(sum_polygon(35), 5940)
    Test.assert_equals(sum_polygon(36), 6120)
    Test.assert_equals(sum_polygon(37), 6300)
    Test.assert_equals(sum_polygon(38), 6480)
    Test.assert_equals(sum_polygon(39), 6660)
    Test.assert_equals(sum_polygon(40), 6840)
    Test.assert_equals(sum_polygon(41), 7020)
    Test.assert_equals(sum_polygon(42), 7200)
    Test.assert_equals(sum_polygon(43), 7380)
    Test.assert_equals(sum_polygon(44), 7560)
    Test.assert_equals(sum_polygon(45), 7740)
    Test.assert_equals(sum_polygon(46), 7920)
    Test.assert_equals(sum_polygon(47), 8100)
    Test.assert_equals(sum_polygon(48), 8280)
    Test.assert_equals(sum_polygon(49), 8460)
    Test.assert_equals(sum_polygon(50), 8640)
    Test.assert_equals(sum_polygon(51), 8820)
    Test.assert_equals(sum_polygon(52), 9000)
    Test.assert_equals(sum_polygon(53), 9180)
    Test.assert_equals(sum_polygon(54), 9360)
    Test.assert_equals(sum_polygon(55), 9540)
    Test.assert_equals(sum_polygon(56), 9720)
    Test.assert_equals(sum_polygon(57), 9900)
    Test.assert_equals(sum_polygon(58), 10080)
    Test.assert_equals(sum_polygon(59), 10260)
    Test.assert_equals(sum_polygon(60), 10440)
    Test.assert_equals(sum_polygon(61), 10620)
    Test.assert_equals(sum_polygon(62), 10800)
    Test.assert_equals(sum_polygon(63), 10980)
    Test.assert_equals(sum_polygon(64), 11160)
    Test.assert_equals(sum_polygon(65), 11340)
    Test.assert_equals(sum_polygon(66), 11520)
    Test.assert_equals(sum_polygon(67), 11700)
    Test.assert_equals(sum_polygon(68), 11880)
    Test.assert_equals(sum_polygon(69), 12060)
    Test.assert_equals(sum_polygon(70), 12240)
    Test.assert_equals(sum_polygon(71), 12420)
    Test.assert_equals(sum_polygon(72), 12600)
    Test.assert_equals(sum_polygon(73), 12780)
    Test.assert_equals(sum_polygon(74), 12960)
    Test.assert_equals(sum_polygon(75), 13140)
    Test.assert_equals(sum_polygon(76), 13320)
    Test.assert_equals(sum_polygon(77), 13500)
    Test.assert_equals(sum_polygon(78), 13680)
    Test.assert_equals(sum_polygon(79), 13860)
    Test.assert_equals(sum_polygon(80), 14040)
    Test.assert_equals(sum_polygon(81), 14220)
    Test.assert_equals(sum_polygon(82), 14400)
    Test.assert_equals(sum_polygon(83), 14580)
    Test.assert_equals(sum_polygon(84), 14760)
    Test.assert_equals(sum_polygon(85), 14940)
    Test.assert_equals(sum_polygon(86), 15120)
    Test.assert_equals(sum_polygon(87), 15300)
    Test.assert_equals(sum_polygon(88), 15480)
    Test.assert_equals(sum_polygon(89), 15660)
    Test.assert_equals(sum_polygon(90), 15840)
    Test.assert_equals(sum_polygon(91), 16020)
    Test.assert_equals(sum_polygon(92), 16200)
    Test.assert_equals(sum_polygon(93), 16380)
    Test.assert_equals(sum_polygon(94), 16560)
    Test.assert_equals(sum_polygon(95), 16740)
    Test.assert_equals(sum_polygon(96), 16920)
    Test.assert_equals(sum_polygon(97), 17100)
    Test.assert_equals(sum_polygon(98), 17280)
    Test.assert_equals(sum_polygon(99), 17460)
