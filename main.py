crosszero_table = [[None, None, None], [None, None, None], [None, None, None]]
def game_table(table1):
    print(" ", end=" ")
    for i in range(1, len(table1[0])+1):
        print(f'{i} ', end="")
    print("")
    for i, value1 in enumerate(table1):
        print(i+1, end=" ")
        for j, value2 in enumerate(value1):
            if value2 is None:
                print("-", end=" ")
            elif value2:
                print('X', end=" ")
            else:
                print(0, end=" ")
        print("")
result = "Ничья"
symbol = 0
for i in range(9):
    if symbol == 0:
        symbol = 'X'
        bool1 = True
    else:
        symbol = 0
        bool1 = False
    cell = input(f'введите через пробел номер строки и столбца для постановки "{symbol}": ')
    cell = list(map(lambda x: int(x) - 1, cell.split()))
    crosszero_table[cell[0]][cell[1]] = bool1
    game_table(crosszero_table)
    if any([all([crosszero_table[cell[0]][0] == bool1, crosszero_table[cell[0]][1] == bool1, crosszero_table[cell[0]][2] == bool1]),
           all([crosszero_table[0][cell[1]] == bool1, crosszero_table[1][cell[1]] == bool1, crosszero_table[2][cell[1]] == bool1]),
           all([crosszero_table[0][0] == bool1, crosszero_table[1][1] == bool1, crosszero_table[2][2] == bool1]),
           all([crosszero_table[0][2] == bool1, crosszero_table[1][1] == bool1, crosszero_table[2][0] == bool1])]):
        result = f"Победа {symbol}"
        break
print(result)
