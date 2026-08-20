print("Ти бачиш печеру. Зайти? ")
answer = input()
if answer == "так":
    print("Ти зайшов у печеру. Тут дуже темно. Запалити смолоскип? ")
    answer = input()
    if answer == "так":
        print("Ти бачиш скриню. Відкрити її? ")
        answer = input()
        if answer == "так":
            print("Це пастка. Тебе зжерли монстри. Кінець гри.")
        else:
            print("Ти пройшов далі.")
    else:
        print("Ти виходиш з печери.")
else:
    print("Ти пішов далі.")
