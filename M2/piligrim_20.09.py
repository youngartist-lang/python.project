cargo = [
    "Руда",
    "Кисень",
    "Аптечка",
    "Насіння",
    "Скафандр",
    "Ящик інструментів",
    "Кава",
]
print(cargo)
backup = cargo.copy()
print(backup)
print(cargo[0:3], cargo[-1])
print(cargo[3])
cargo[3] = "ПОШКОДЖЕНО!"
print(cargo)
if "Кисень" in cargo:
    print(f"Кількість балонів кисню - {cargo.count('Кисень')}")
else:
    print("ТРЕВОГА! НЕМАЄ КИСНЮ!")
cargo.insert(0, "Рятувальна капсула")
print(cargo)
number_sk = cargo.index("Скафандр")
cargo[1], cargo[5] = cargo[5], cargo[1]
print(cargo[0:2])
if "Руда" in cargo:
    number_ruda = cargo.index("Руда")
    print(f"У космос скинуто: {cargo.pop(number_ruda)}")
else:
    print("Руди немає.")
cargo.append(input("Що додати до списку? "))
print(cargo)
cargo.sort(reverse=True)
print(cargo)
