
def greet_rules():
    print("--------------------")
    print(" Добро пожаловать в ")
    print( "игру Крестики-Нолики!")
    print("Правила:игроки по очереди")
    print("на свободные клетки вводят")
    print("по координатам x, y, где")
    print("x-номер строки от 0 до 2")
    print("y-номер столбца от 0 до 2")
    print("знак крестика или нолика")
    print("(один - всегда крестик,")
    print("другой - всегда нолик).")
    print("Первый, кто выстроит три")
    print("своих знака по вертикали,")
    print("горизонтали или диагонали - выиграет.")
    print("----------------------")

field= [[' '] * 3 for i in range(3)]
def show():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()

def ask():
    while True:
        cords = input("         Ваш ход: ").split()

        if len(cords) != 2:
            print(" Введите две координаты от 0 до 2! ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа от 0 до 2! ")
            continue

        x, y = int(x), int(y)

        if x > 2 or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y

def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл Крестик!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл Нолик!!!")
            return True
    return False
check_win()

greet_rules()
# field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = ask()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print(" Ничья!")
        break