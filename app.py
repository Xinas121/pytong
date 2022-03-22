def exp_funct(liczba, potega):
    pom = 1
    pom2 = 1
    while pom <= potega:
        pom2 = pom2*liczba
        pom += 1
    return pom2


x = exp_funct(5, 5)
print(x)
