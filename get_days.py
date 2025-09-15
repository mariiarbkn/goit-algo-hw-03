from datetime import datetime
def get_days_from_today(date_str):
    try:
        given_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return "Помилка: використовуйте формат РРРР-ММ-ДД"
    today = datetime.now().date()
    delta = today - given_date
    return delta.days
date_str = input("Введіть дату у форматі РРРР-ММ-ДД: ")
print(get_days_from_today(date_str))
