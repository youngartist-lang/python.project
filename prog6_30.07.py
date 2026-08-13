gold_quantity = input("Скільки всього золота?: ")
players_quantity = input("Скільки всього гравців?: ")
gold_per_player = int(gold_quantity) // (players_quantity)
print(f"Кожен отримає {gold_per_player} золота.")
