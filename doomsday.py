import datetime
from random import randrange
from datetime import timedelta

week = ['Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday ']


def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


def generate_doomsday():
    start = datetime.datetime(1900, 1, 1)
    end = datetime.datetime(2099, 12, 31)
    day = random_date(start, end)
    print(day.strftime("%Y-%m-%d"))
    input("Press Enter to continue...")
    two_digits = day.year % 100
    if two_digits % 2 ==1:
        two_digits = two_digits +11
    two_digits = two_digits/2
    if two_digits % 2 ==1:
        two_digits +11
    print(f"year's value is {7-(two_digits % 7)}")
    print(week[day.isoweekday()])


if __name__ == "__main__":
    generate_doomsday()
