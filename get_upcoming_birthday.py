
from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        # Перетворюємо рядок у дату
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # Визначаємо день народження у поточному році
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо день народження вже минув, беремо наступний рік (для кінця року)
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)

        # Перевіряємо, чи день народження протягом наступних 7 днів
        if 0 <= (birthday_this_year - today).days <= 7:

           # Встановлюємо дату привітання
            congratulation_date = birthday_this_year

            # Переносимо привітання на понеділок, якщо день народження у вихідний
            if congratulation_date.weekday() == 5:  # Субота
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:  # Неділя
                congratulation_date += timedelta(days=1)

            # Додаємо користувача до результату
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

# Приклад використання
users = [
    {"name": "John Doe", "birthday": "1985.11.01"},
    {"name": "Jane Smith", "birthday": "1990.11.05"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)