player_gold = 100
potion_prise = 25
player_name = input("Привіт, мандрівнику! Як тебе звати? ")
print(f"Вітаю в моєму магазині, {player_name}!")
print(f"У твоєму гаманці зараз є {player_gold} монет золота.")
potion_to_buy = int(input("Скільки зілля здоров'я хочеш купити? "))
total_cost = potion_to_buy * potion_prise
remaining_gold = player_gold - total_cost
print(f"Успішно! Ти купив {potion_to_buy}шт. зілля і витратив {total_cost} золота. ")
print(f"Залишок в гаманці: {remaining_gold} монет.")
