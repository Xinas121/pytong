import random

# o statek
# x trafiony statek
# m nie trafiony strzal


def generate_map():  # generacja mapy do gry
    while True:
        print("podaj wymiar mapy")
        wymiar = int(input())
        if wymiar <= 4:
            print("za mala mapa. musi być większa niż 4")
        else:
            wymiar_tab = [[' '] * wymiar for i in range(wymiar)]
            map_destro = [[' '] * wymiar for i in range(wymiar)]
            map_destro2 = [[' '] * wymiar for i in range(wymiar)]
            map_2 = [[' '] * wymiar for i in range(wymiar)]
            return wymiar_tab, map_destro, map_destro2, map_2, wymiar


def place_warship_2():  # ustawianie statków
    for num in range(dimension):
        print(map_player[num])
    ship_count = 0
    print("Gdzie chcesz ustawic statek pozycje x i y")
    x = int(input())
    y = int(input())
    print("w którym kierunku ustawiać od punktu startowego. prawo/lewo/gora/dol")
    position = input()
    match position:
        case "prawo":
            if x == dimension and not (x == dimension and y == 1) and not (x == dimension and y == dimension):
                print("prawa granica mapy nie można ustawic statku skierowanego w prawo")
                print("podaj nowe pozycje")
                place_warship_2()
            elif x == dimension and (x == dimension and y == 1) and not (x == dimension and y == dimension):
                print(
                    "prawy gorny rog mapy nie można ustawic statku skierowanego w prawo lub gore")
                print("podaj nowe pozycje")
                place_warship_2()
            elif x == dimension and not (x == dimension and y == 1) and (x == dimension and y == dimension):
                print(
                    "prawy dolny rog mapy nie można ustawic statku skierowanego w prawo lub dol")
                print("podaj nowe pozycje")
                place_warship_2()
            else:
                map_warship_destroy_check[x-1][y-1] = ship_count
                map_warship_destroy_check[x-1][y] = ship_count
                map_player[x-1][y-1] = "o"
                map_player[x-1][y] = "o"
                ship_count += 1

                return ship_count
        case "dol":
            if y == dimension and not (y == dimension and x == 1) and (y == dimension and x == dimension):
                print(
                    "prawy dolny rog mapy nie można ustawic statku skierowanego w prawo lub dol")
                print("podaj nowe pozycje")
                place_warship_2()
            elif y == dimension and not (y == dimension and x == 1) and not (y == dimension and x == dimension):
                print("dolna granica mapy nie mozna ustawic statku w dol")
                print("podaj nowe pozycje")
                place_warship_2()
            elif y == dimension and (y == dimension and x == 1) and not (y == dimension and x == dimension):
                print("lewy dolny rog mapy nie mozna ustawic statku w dol i w lewo")
                print("podaj nowe pozycje")
                place_warship_2()
            else:
                map_warship_destroy_check[x-1][y-1] = ship_count
                map_warship_destroy_check[x][y-1] = ship_count
                map_player[x-1][y-1] = "o"
                map_player[x][y-1] = "o"
                ship_count += 1
                return ship_count

        case "lewo":
            if x == 1 and not (x == 1 and y == dimension) and not (x == 1 and y == 1):
                print("lewa granica mapy nie można ustawic statku skierowanego w lewo")
                print("podaj nowe pozycje")
                place_warship_2()
            elif x == 1 and (x == 1 and y == dimension) and not (x == 1 and y == 1):
                print(
                    "lewy dolny rog mapy nie można ustawic statku skierowanego w lewo i dol")
                print("podaj nowe pozycje")
                place_warship_2()
            elif x == 1 and not (x == 1 and y == dimension) and (x == 1 and y == 1):
                print(
                    "lewy gorny rog mapy nie można ustawic statku skierowanego w lewo i dol")
                print("podaj nowe pozycje")
                place_warship_2()
            else:
                map_warship_destroy_check[x-1][y-1] = ship_count
                map_warship_destroy_check[x-1][y-2] = ship_count
                map_player[x-1][y-1] = "o"
                map_player[x-1][y-2] = "o"
                ship_count += 1
                return ship_count
        case "gora":
            if x == 1 and not(x == 1 and y == dimension) and not (x == 1 and y == 1):
                print("gorna granica mapy nie mozna ustawic statku w gore")
                print("podaj nowe pozycje")
                place_warship_2()
            elif x == 1 and y == 1:
                print("lewy gorny rog mapy nie mozna ustawic statku w gore i lewo")
                print("podaj nowe pozycje")
                place_warship_2()
            elif x == dimension and (x == dimension and y == 1) and not (x == dimension and y == dimension):

                print("prawy gorny rog mapy nie mozna ustawic statku w gore i prawo")
                print("podaj nowe pozycje")
                place_warship_2()
            else:
                map_warship_destroy_check[x-1][y-1] = ship_count
                map_warship_destroy_check[x-2][y-1] = ship_count
                map_player[x-1][y-1] = "o"
                map_player[x-2][y-1] = "o"
                ship_count += 1
                return ship_count


def warship_player_shot():
    licznik = 0
    print("Podaj pozycje x i y strzału")
    x = int(input())
    y = int(input())
    if map_npc[x-1][y-1] == "o":
        print("statek trafiony")
        map_npc[x-1][y-1] = "x"
        map_destro_npc[x-1][y-1] = "x"
        for num in range(dimension):
            cnt = map_destro_npc[num].count(0)
            licznik = licznik+cnt
        if licznik == 0:
            print('statek zniszczony')
        return map_npc
    else:
        map_npc[x-1][y-1] = "m"
        print("pudlo")
        return map_npc

    # npc_ship_counter = 0
    # x = random.randint(0, dimension)
    # y = random.randint(0, dimension)
    # pos = random.randint(0, 4)


def warship_npc_shot():
    npc_shot_count = 0
    x = random.randint(0, dimension)
    y = random.randint(0, dimension)
    pos = random.randint(0, 4)
    if map_player[x][y] == "o":
        map_player[x][y] == "x"
        map_warship_destroy_check[x][y] == "x"
        for num in range(dimension):
            cnt = map_warship_destroy_check[num].count(0)
            npc_shot_count += cnt
        if npc_shot_count == 0:
            print("twoj statek został zniszczony")
        return map_player
    else:
        map_player[x][y] = "m"
        return map_player


def npc_ship_place_2():  # ustawianie statków
    npc_ship_counter = 0
    x = random.randint(1, dimension+1)
    y = random.randint(1, dimension+1)
    pos = random.randint(0, 4)
    match pos:
        case 0:
            if x == dimension and not (x == dimension and y == 1) and not (x == dimension and y == dimension):
                npc_ship_place_2()
            elif x == dimension and (x == dimension and y == 1) and not (x == dimension and y == dimension):
                npc_ship_place_2()
            elif x == dimension and not (x == dimension and y == 1) and (x == dimension and y == dimension):
                npc_ship_place_2()
            else:
                map_destro_npc[x-1][y-1] = npc_ship_counter
                map_destro_npc[x-1][y] = npc_ship_counter
                map_npc[x-1][y-1] = "o"
                map_npc[x-1][y] = "o"
                npc_ship_counter += 1
                return npc_ship_counter
        case 1:
            if y == dimension and not (y == dimension and x == 1) and (y == dimension and x == dimension):
                npc_ship_place_2()
            elif y == dimension and not (y == dimension and x == 1) and not (y == dimension and x == dimension):
                npc_ship_place_2()
            elif y == dimension and (y == dimension and x == 1) and not (y == dimension and x == dimension):
                npc_ship_place_2()
            else:
                map_destro_npc[x-1][y-1] = npc_ship_counter
                map_destro_npc[x][y-1] = npc_ship_counter
                map_npc[x-1][y-1] = "o"
                map_npc[x][y-1] = "o"
                return npc_ship_counter

        case 2:
            if x == 1 and not (x == 1 and y == dimension) and not (x == 1 and y == 1):
                npc_ship_place_2()
            elif x == 1 and (x == 1 and y == dimension) and not (x == 1 and y == 1):
                npc_ship_place_2()
            elif x == 1 and not (x == 1 and y == dimension) and (x == 1 and y == 1):
                npc_ship_place_2()
            else:
                map_destro_npc[x-1][y-1] = npc_ship_counter
                map_destro_npc[x-1][y-2] = npc_ship_counter
                map_npc[x-1][y-1] = "o"
                map_npc[x-1][y-2] = "o"
                return npc_ship_counter
        case 3:
            if x == 1 and not(x == 1 and y == dimension) and not (x == 1 and y == 1):
                npc_ship_place_2()
            elif x == 1 and y == 1:
                npc_ship_place_2()
            elif x == dimension and (x == dimension and y == 1) and not (x == dimension and y == dimension):
                npc_ship_place_2()
            else:
                map_destro_npc[x-1][y-1] = npc_ship_counter
                map_destro_npc[x-2][y-1] = npc_ship_counter
                map_npc[x-1][y-1] = "o"
                map_npc[x-2][y-1] = "o"
                return npc_ship_counter


map_player, map_warship_destroy_check, map_destro_npc, map_npc, dimension = generate_map()

ship_amount = place_warship_2()
npc_ship_amount = npc_ship_place_2()
for num in range(dimension):
    print(map_npc[num])

# for num in range(dimension):
#     print("destro czek", map_warship_destroy_check[num])

for num in range(0, 2):
    warship_player_shot()
    warship_npc_shot()

for num in range(dimension):
    print(map_player[num])
