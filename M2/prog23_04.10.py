inventory = ["Меч", "Зілля", "Ключ", "Гриб", 100, 150]

for item in inventory:
    print(item)
print("Завершено")

for letter in "Python":
    print(letter)

numbers2 = [1, 2, 3, 3, 2, 3]
count_number = 0
print(numbers2)
for number in numbers2:
    print(number)
for number in numbers2:
    if number != 2:
        numbers2.append(number)
    else:
        count_number += 1
print(numbers2)
