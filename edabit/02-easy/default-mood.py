"""
Default Mood
Create a function that takes in a current mood and return a sentence in the following format:
"Today, I am feeling {mood}". However, if no argument is passed, return "Today, I am feeling neutral".

Examples
mood_today("happy") ➞ "Today, I am feeling happy"

mood_today("sad") ➞ "Today, I am feeling sad"

mood_today() ➞ "Today, I am feeling neutral"
Notes
Check the Resources tab for some helpful information.
"""

from edabit.Test import Test


def mood_today(mood):
    if len(mood) != 0:
        return "Today, I am feeling " + str(mood)
    else:
        return "Today, I am feeling neutral"


if __name__ == '__main__':
    Test.assert_equals(mood_today("happy"), "Today, I am feeling happy")
    Test.assert_equals(mood_today("sad"), "Today, I am feeling sad")
    Test.assert_equals(mood_today("very happy"), "Today, I am feeling very happy")
    Test.assert_equals(mood_today("rather empty inside"), "Today, I am feeling rather empty inside")
    Test.assert_equals(mood_today("confused"), "Today, I am feeling confused")
    Test.assert_equals(mood_today(""), "Today, I am feeling neutral")
