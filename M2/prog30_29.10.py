pin = "1234"
attempts = 0

while True:
    code = input("Введіть PIN-код: ")
    if code == " ":
        print("PIN-код не може бути порожнім. Спробуйте ще раз.")
        continue

    attempts += 1

    if code == pin:
        print("Доступ дозволено.")
        break
    else:
        print("Невірний PIN-код.")
        if attempts >= 3:
            print("Заблоковано після 3 невдалих спроб.")
            break
