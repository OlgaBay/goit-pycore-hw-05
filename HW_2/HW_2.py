import re
from typing import Callable


# Знаходить дійсні числа в тексті та послідовно повертає їх
def generator_numbers(text: str):
    pattern = r"\d+\.\d+"
    
    for word in text.split():
        income = re.findall(pattern, word)

        if income:
            # Передає знайдене число як float через генератор
            yield float(income[0])


# Обчислює суму чисел, отриманих від переданої функції-генератора
def sum_profit(text: str, func: Callable) -> float:
    total = 0

    for num in func(text):
        total += num

    return total


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)

if total_income != 0:
    print(f"Загальний дохід: {total_income} доларів.")
else:
    print("Працівник не отримав доходу.")