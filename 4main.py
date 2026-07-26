from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.05.23"},
    {"name": "Jane Smith", "birthday": "1990.07.29"}
]

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    result = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        try:
            birthday_this_year = birthday.replace(year=today.year)
        except ValueError:
            birthday_this_year = birthday.replace(year=today.year, day=28) + timedelta(days=1)

        if birthday_this_year < today:
            try:
                birthday_this_year = birthday.replace(year=today.year + 1)
            except ValueError:
                birthday_this_year = birthday.replace(year=today.year + 1, day=28) + timedelta(days=1)

        difference = (birthday_this_year - today).days

        if 0 <= difference <= 7:
            if birthday_this_year.weekday() == 5:
                birthday_this_year += timedelta(days=2)
            elif birthday_this_year.weekday() == 6:
                birthday_this_year += timedelta(days=1)

            result.append({
                "name": user["name"],
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
            })

    return result

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
