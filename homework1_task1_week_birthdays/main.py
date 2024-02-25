from datetime import datetime
from datetime import timedelta


def get_next_week(today: datetime.date) -> list[datetime.date]:  # returns a list of dates within one week from today
    one_day = timedelta(days=1)
    week = []
    for _ in range(7):
        week.append((today.month, today.day))
        today += one_day
    return week


def convert_date_to_day(date: datetime) -> str:
    """
    Returns name of day.\n
    For example: datetime(2022, 2, 24) -> "Thursday"

    :param date: in datetime format
    :return: name of the day
    """
    week = {0: "Monday",
            1: "Tuesday",
            2: "Wednesday",
            3: "Thursday",
            4: "Friday",
            5: "Saturday",
            6: "Sunday"}
    return week[date.weekday()]


def get_birthdays_per_week(users: list[dict]):
    work_week_greetings = {"Monday": [],
                           "Tuesday": [],
                           "Wednesday": [],
                           "Thursday": [],
                           "Friday": []}

    today = datetime.now().date()
    actual_week = get_next_week(today)

    for user in users:  # {"name": "Michael", "birthday": datetime(1995, 1, 16)}
        if (user["birthday"].month, user["birthday"].day) in actual_week:
            user_birthday = datetime(today.year, user["birthday"].month, user["birthday"].day)
            day_of_week = convert_date_to_day(user_birthday)
            if day_of_week in ("Saturday", "Sunday"):
                work_week_greetings["Monday"].append(user["name"])
            else:
                work_week_greetings[day_of_week].append(user["name"])

    for day, names in work_week_greetings.items():
        print("{}: {}".format(day, ", ".join(names)))

    pass


if __name__ == "__main__":
    list_of_users = [{"name": "Michael", "birthday": datetime(1995, 1, 16)},
                     {"name": "Angela", "birthday": datetime(1997, 2, 27)},
                     {"name": "Lucy", "birthday": datetime(1993, 3, 2)},
                     {"name": "Lucy", "birthday": datetime(1991, 3, 2)},
                     {"name": "Gregor", "birthday": datetime(1993, 3, 3)},
                     {"name": "Anton Vyshnevskii", "birthday": datetime(1996, 2, 25)},
                     {"name": "Brandon", "birthday": datetime(1993, 3, 6)}]
    get_birthdays_per_week(list_of_users)
    print()
    print("24.02.2022 was {}".format(convert_date_to_day(datetime(2022, 2, 24))))
