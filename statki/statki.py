import random

# o statek
# x trafiony statek
# m nie trafiony strzal


def generate_map():  # generacja mapy do gry
    while True:
        print("podaj wymiary mapy")
        wymiar = int(input())
        if wymiar <= 4:
            print("za mala mapa. musi być większa niż 4")
        else:
            wymiar_tab = [[' '] * wymiar for i in range(wymiar)]
            return wymiar_tab, wymiar


def place_warship_2(map_for_warships_player, wymiar):  # ustawianie statków
    for num in range(wymiar):
        print(map_for_warships_player[num])
    print("Gdzie chcesz ustawic statek pozycje x i y")
    x = int(input())
    y = int(input())
    print("w którym kierunku ustawiać od punktu startowego. prawo/lewo/gora/dol")
    position = input()
    match position:
        case "prawo":
            if x == wymiar and not (x == wymiar and y == 1) and not (x == wymiar and y == wymiar):
                print("prawa granica mapy nie można ustawic statku skierowanego w prawo")
            if x == wymiar and (x == wymiar and y == 1) and not (x == wymiar and y == wymiar):
                print(
                    "prawy gorny rog mapy nie można ustawic statku skierowanego w prawo lub gore")
            if x == wymiar and not (x == wymiar and y == 1) and (x == wymiar and y == wymiar):
                print(
                    "prawy dolny rog mapy nie można ustawic statku skierowanego w prawo lub dol")
            else:
                map_for_warships_player[x-1][y-1] = "o"
                map_for_warships_player[x-1][y] = "o"
                return map_for_warships_player
        case "dol":
            if y == wymiar and not (y == wymiar and x == 1) and (y == wymiar and x == wymiar):
                print(
                    "prawy dolny rog mapy nie można ustawic statku skierowanego w prawo lub dol")
            if y == wymiar and not (y == wymiar and x == 1) and not (y == wymiar and x == wymiar):
                print("dolna granica mapy nie mozna ustawic statku w dol")
            if y == wymiar and (y == wymiar and x == 1) and not (y == wymiar and x == wymiar):
                print("lewy dolny rog mapy nie mozna ustawic statku w dol i w lewo")
            else:
                map_for_warships_player[x-1][y-1] = "o"
                map_for_warships_player[x][y-1] = "o"
                return map_for_warships_player

        case "lewo":
            if x == 1 and not (x == 1 and y == wymiar) and not (x == 1 and y == 1):
                print("lewa granica mapy nie można ustawic statku skierowanego w lewo")
            if x == 1 and (x == 1 and y == wymiar) and not (x == 1 and y == 1):
                print(
                    "lewy dolny rog mapy nie można ustawic statku skierowanego w lewo i dol")
            if x == 1 and not (x == 1 and y == wymiar) and (x == 1 and y == 1):
                print(
                    "lewy gorny rog mapy nie można ustawic statku skierowanego w lewo i dol")
            else:
                map_for_warships_player[x-1][y-1] = "o"
                map_for_warships_player[x-1][y-2] = "o"
                return map_for_warships_player
        case "gora":
            if x == 1 and not(x == 1 and y == wymiar) and not (x == 1 and y == 1):
                print("gorna granica mapy nie mozna ustawic statku w gore")
            if x == 1 and (x == 1 and y == wymiar) and not (x == 1 and y == 1):
                print("lewy gorny rog mapy nie mozna ustawic statku w gore i lewo")
            if x == 1 and not (x == 1 and y == wymiar) and (x == 1 and y == 1):
                print("prawy gorny rog mapy nie mozna ustawic statku w gore i prawo")
            else:
                map_for_warships_player[x-1][y-1] = "o"
                map_for_warships_player[x-2][y-1] = "o"
                return map_for_warships_player


map_clean, dimension = generate_map()
map_player = place_warship_2(map_clean, dimension)
print(map_player[0][0])
for num in range(dimension):
    print(map_player[num])
