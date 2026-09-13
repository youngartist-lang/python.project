import random

answers = [
    "Точно так",
    "Обов'язково",
    "Можливо",
    "Колись",
    "Не знаю",
    "Точно ні",
    "Ніколи",
    "Навіть не мрій",
]

input("Задай кулі питання: ")

random_answer = random.choice(answers)

print(f"Куля відповіла: {random_answer}")
