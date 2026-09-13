piece_of_pizza = int(input("Скільки шматків піци ви можете з'їсти?"))
piece_pizza = int(input("Скільки шматків піци в коробці?"))
if piece_of_pizza < 0:
    print("Ти що збираєшся випльовувати піцу?")
else:
    if piece_of_pizza > piece_pizza:
        print("Замовляємо ще одну піцу!")
    if piece_of_pizza <= piece_pizza:
        print("Смачного!")
