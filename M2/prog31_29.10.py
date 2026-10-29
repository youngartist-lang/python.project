import random

number = random.randint(1, 100)
max_attempts = 7
attempts = 0
won = False

print("Вгадай число від 1 до 100. У тебе є 7 спроб.")
while attempts < max_attempts:
    answer = input("Введіть число: ")
    if answer == "":
        print("Будь ласка, введіть дійсне число.")
        continue

    answer = int(answer)
    attempts += 1

    if answer == number:
         print(f"Вітаємо! Ви вгадали число {number} за {attempts} спроб.")
         won = True
         break
    elif answer < number:
         print("Загадане число більше.")
    else:
        print("Загадане число менше.")

if not won:
    print(f"Ви не вгадали число. Загадане число було {number}.")