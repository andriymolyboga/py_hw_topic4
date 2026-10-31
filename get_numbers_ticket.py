
import random

def get_numbers_ticket(min, max, quantity):
    # Перевіряємо коректність параметрів
    if (min < 1 or max > 1000 or min >= max
            or quantity < 1 or quantity > (max - min + 1)):
        return "Введені некоректні параметри."

    # Генеруємо унікальні випадкові числа
    numbers = random.sample(range(min, max + 1), quantity)

    # Сортуємо числа
    return sorted(numbers)


# Перевірка роботи функції
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

lottery_numbers = get_numbers_ticket(1, 2000, 3)
print("Ваші лотерейні числа:", lottery_numbers)
