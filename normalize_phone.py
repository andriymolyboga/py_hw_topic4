import re

def normalize_phone(phone_number):
    # Видаляємо всі символи, крім цифр та '+'
    phone_number = re.sub(r'[^\d+]', '', phone_number)

    # Якщо номер починається з '+', залишаємо його без змін
    if phone_number.startswith('+'):
        return phone_number

    # Якщо номер починається з '380', додаємо лише '+'
    if phone_number.startswith('380'):
        return '+' + phone_number

    # Якщо міжнародного коду немає, додаємо '+38'
    return '+38' + phone_number

raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = []

for num in raw_numbers:
    normalized = normalize_phone(num)
    sanitized_numbers.append(normalized)


print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)