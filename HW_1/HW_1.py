# Створює та повертає функцію для обчислення чисел Фібоначчі з кешуванням
def caching_fibonacci():
    cache = {}

    # Обчислює n-те число Фібоначчі з використанням кешування
    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        
        # Повертаємо раніше обчислене значення з кешу
        if n in cache:
            return cache[n]
        
        # Обчислюємо нове значення та зберігаємо його в кеші
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
      
    return fibonacci


fib = caching_fibonacci()

while True:
    user_input = input("Введіть номер числа Фібоначчі, яке хочете обчислити (або 'exit' для виходу): ")

    if user_input.strip().lower() == 'exit':
        print("До зустрічі!")
        break

    try:
        n = int(user_input)
        print(f"Число Фібоначчі дорівнює: {fib(n)}")
    except ValueError:
        print("Помилка, введіть ціле число.")

  
    