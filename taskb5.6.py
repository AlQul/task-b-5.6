def nacalo():
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")

def doska():
    print(f"  0 1 2")
    for i in range(3):
        row_info = " ".join(pole[i])
        print(f"{i} {row_info}")

def ask():
    while True:
        cords = input("Сделайте ход: ").split()
        if len(cords) != 2:
            print("Введите 2 координаты! ")
            continue
        x, y = cords
        if not (x.isdigit()) or not (y.isdigit()):
            print("Введите числа! ")
            continue
        x, y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Координаты вне диапазона! ")
            continue
        if pole[x][y] != " ":
            print("Клетка занята! ")
            continue
        return x, y

def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(pole[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False

nacalo()
pole = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    doska()
    if count % 2 == 1:
        print(" Ходит X!")
    else:
        print(" Ходит 0!")
    x, y = ask()
    if count % 2 == 1:
        pole[x][y] = "X"
    else:
        pole[x][y] = "0"
    if check_win():
        break
    if count == 9:
        print("Ничья!")
        break