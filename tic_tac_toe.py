# Warunki zakończenia
# lose  if (stan_gry1[0] == "O" and stan_gry1[1] == "O" and stan_gry1[2] == "O" or stan_gry2[0] == "O" and stan_gry2[1] == "O" and stan_gry2[2] == "O" or stan_gry3[0] == "O" and stan_gry3[1] == "O" and stan_gry3[2] == "O" or stan_gry1[0] == "O" and stan_gry2[1] == "O" and stan_gry3[2] == "O" or stan_gry3[0] == "O" and stan_gry2[1] == "O" and stan_gry1[2] == "O" or stan_gry1[0] == "O" and stan_gry2[0] == "O" and stan_gry3[0] == "O" or stan_gry1[1] == "O" and stan_gry2[1] == "O" and stan_gry3[1] == "O" or stan_gry1[2] == "O" and stan_gry2[2] == "O" and stan_gry3[2] == "O") {
# win if (stan_gry1[0] == "X" and stan_gry1[1] == "X" and stan_gry1[2] == "X" or stan_gry2[0] == "X" and stan_gry2[1] == "X" and stan_gry2[2] == "X" or stan_gry3[0] == "X" and stan_gry3[1] == "X" and stan_gry3[2] == "X" or stan_gry1[0] == "X" and stan_gry2[1] == "X" and stan_gry3[2] == "X" or stan_gry3[0] == "X" and stan_gry2[1] == "X" and stan_gry1[2] == "X" or stan_gry1[0] == "X" and stan_gry2[0] == "X" and stan_gry3[0] == "X" or stan_gry1[1] == "X" and stan_gry2[1] == "X" and stan_gry3[1] == "X" or stan_gry1[2] == "X" and stan_gry2[2] == "X" and stan_gry3[2] == "X") {
# draw      if przeszukanie tablicy i sprawdzenie czy nie jest placeholder gdzies
import random


def random_bot():
    y = random.randint(1, 9)
    if y == 1 and (stan_gry1[0] == "X" or stan_gry1[0] == "O"):
        y = random_bot()
    elif y == 1 and stan_gry1[0] == ' ':
        stan_gry1[0] = 'X'
    if y == 2 and (stan_gry1[1] == "X" or stan_gry1[1] == "O"):
        y = random_bot()
    elif y == 2 and stan_gry1[1] == ' ':
        stan_gry1[1] = 'X'
    if y == 3 and (stan_gry1[2] == "X" or stan_gry1[2] == "O"):
        y = random_bot()
    elif y == 3 and stan_gry1[2] == ' ':
        stan_gry1[2] = 'X'
    if y == 4 and (stan_gry2[0] == "X" or stan_gry2[0] == "O"):
        y = random_bot()
    elif y == 4 and stan_gry2[0] == ' ':
        stan_gry2[0] = 'X'
    if y == 5 and (stan_gry2[1] == "X" or stan_gry2[1] == "O"):
        y = random_bot()
    elif y == 5 and stan_gry2[1] == ' ':
        stan_gry2[1] = 'X'
    if y == 6 and (stan_gry2[2] == "X" or stan_gry2[2] == "O"):
        y = random_bot()
    elif y == 6 and stan_gry2[2] == ' ':
        stan_gry2[2] = 'X'
    if y == 7 and (stan_gry3[0] == "X" or stan_gry3[0] == "O"):
        y = random_bot()
    elif y == 7 and stan_gry3[0] == ' ':
        stan_gry3[0] = 'X'
    if y == 8 and (stan_gry3[1] == "X" or stan_gry3[1] == "O"):
        y = random_bot()
    elif y == 8 and stan_gry3[1] == ' ':
        stan_gry3[1] = 'X'
    if y == 9 and (stan_gry3[2] == "X" or stan_gry3[2] == "O"):
        y = random_bot()
    elif y == 9 and stan_gry3[2] == ' ':
        stan_gry3[2] = 'X'
    return y, stan_gry1, stan_gry2, stan_gry3


stan_gry1 = [' ']*3  # pierwsza linia mapy
stan_gry2 = [' ']*3  # druga linia mapy
stan_gry3 = [' ']*3  # trzecia linia mapy
Pom = 1
# print(stan_gry1)
# print(stan_gry2)
# print(stan_gry3)
print("Tic-tac-toe Game")

while Pom == 1:
    print("podaj liczbe 1-9 gdzie chcesz wstawić O. Liczone od lewej gory")
    x = input()
    match x:
        case "1":
            stan_gry1[0] = "O"
        case "2":
            stan_gry1[1] = "O"
        case "3":
            stan_gry1[2] = "O"
        case "4":
            stan_gry2[0] = "O"
        case "5":
            stan_gry2[1] = "O"
        case "6":
            stan_gry2[2] = "O"
        case "7":
            stan_gry3[0] = "O"
        case "8":
            stan_gry3[1] = "O"
        case "9":
            stan_gry3[2] = "O"

    if (stan_gry1[0] == "O" and stan_gry1[1] == "O" and stan_gry1[2] == "O") or \
        (stan_gry2[0] == "O" and stan_gry2[1] == "O" and stan_gry2[2] == "O") or \
        (stan_gry3[0] == "O" and stan_gry3[1] == "O" and stan_gry3[2] == "O") or \
        (stan_gry1[0] == "O" and stan_gry2[1] == "O" and stan_gry3[2] == "O") or \
        (stan_gry3[0] == "O" and stan_gry2[1] == "O" and stan_gry1[2] == "O") or \
        (stan_gry1[0] == "O" and stan_gry2[0] == "O" and stan_gry3[0] == "O") or \
        (stan_gry1[1] == "O" and stan_gry2[1] == "O" and stan_gry3[1] == "O") or \
            (stan_gry1[2] == "O" and stan_gry2[2] == "O" and stan_gry3[2] == "O"):
        print("Wygrales brawo")
        Pom = 0
        break
    zwrot, stan_gry1, stan_gry2, stan_gry3 = random_bot()
    if (stan_gry1[0] == "X" and stan_gry1[1] == "X" and stan_gry1[2] == "X") or \
        (stan_gry2[0] == "X" and stan_gry2[1] == "X" and stan_gry2[2] == "X") or \
        (stan_gry3[0] == "X" and stan_gry3[1] == "X" and stan_gry3[2] == "X") or \
        (stan_gry1[0] == "X" and stan_gry2[1] == "X" and stan_gry3[2] == "X") or \
        (stan_gry3[0] == "X" and stan_gry2[1] == "X" and stan_gry1[2] == "X") or \
        (stan_gry1[0] == "X" and stan_gry2[0] == "X" and stan_gry3[0] == "X") or \
        (stan_gry1[1] == "X" and stan_gry2[1] == "X" and stan_gry3[1] == "X") or \
            (stan_gry1[2] == "X" and stan_gry2[2] == "X" and stan_gry3[2] == "X"):
        print("przegrales zlamasie")
        Pom = 0
        break
    if stan_gry1[0] != ' ' and stan_gry1[1] != ' ' and stan_gry1[2] != ' ' and stan_gry2[0] != ' ' and \
            stan_gry2[0] != ' ' and stan_gry2[1] != ' ' and stan_gry2[2] != ' ' and \
            stan_gry3[0] != ' ' and stan_gry3[1] != ' ' and stan_gry3[2] != ' ':
        print("remis")
        Pom = 0
        break
    print(stan_gry1)
    print(stan_gry2)
    print(stan_gry3)
print(stan_gry1)
print(stan_gry2)
print(stan_gry3)
