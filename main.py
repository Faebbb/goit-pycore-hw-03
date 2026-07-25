from datetime import datetime


input_date = input("Введіть дату у форматі РРРР-ММ-ДД: ")

def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, "%Y-%m-%d").date()

        today = datetime.today().date()

        distance = today - input_date

        return distance.days

    except ValueError:
        return "Неправильний формат дати. Використовуйте формат РРРР-ММ-ДД."

print(get_days_from_today(input_date))