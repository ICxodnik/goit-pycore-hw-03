from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.03.23"},
    {"name": "Jane Smith", "birthday": "1990.03.27"}
]
# 6 не 7, тому що рахуємо поточний день за 7
MAX_CONG_RANGE = 6


#дає список приітань на цей робочий тиждень
def get_upcoming_birthdays(users):
    today = datetime.today().date()
    max_range = today + timedelta(days = MAX_CONG_RANGE)
    # список привітальників
    cong_list = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date().replace(year = today.year)
        
        # Переносимо день народження тих хто народився в субботу
        if birthday.weekday() == 5:
            birthday = birthday + timedelta(days = 2)

        # Переносимо день народження тих хто народився в неділю
        if birthday.weekday() == 6:
            birthday = birthday + timedelta(days = 1)

        # Відсіюємо дні народження лише після врахування коректування дня вітання
        if birthday < today or birthday > max_range:
            continue

        cong_list.append({"name": user["name"], "congratulation_date": birthday.strftime("%Y.%m.%d")})

    return cong_list

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
