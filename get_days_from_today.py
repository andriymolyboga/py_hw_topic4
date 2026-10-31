
from datetime import datetime

def get_days_from_today(date):
    """
    Розраховує кількість днів між заданою датою та сьогоднішньою датою.

    Args:
        date (str): Дата у форматі 'YYYY-MM-DD'.

    Returns:
        int: Кількість днів від заданої дати до сьогоднішньої.
             Від'ємне число, якщо задана дата в майбутньому.
        None: Якщо формат дати неправильний.
    """
    try:
        # Перетворюємо рядок на об'єкт datetime
        input_date = datetime.strptime(date, "%Y-%m-%d")

        # Отримуємо поточну дату без урахування часу
        today = datetime.today().date()

        # Перетворюємо задану дату на date
        input_date = input_date.date()

        # Розраховуємо різницю між датами
        difference = today - input_date

        return difference.days

    except (ValueError, TypeError):
        return "Ви ввели неправильний формат дати. Будь ласка, використовуйте формат 'YYYY-MM-DD'."
    


# Приклади використання
print(get_days_from_today("2025-12-10"))
print(get_days_from_today("2027-12-10"))
print(get_days_from_today("не дата"))
print(get_days_from_today("2027-13-10"))
