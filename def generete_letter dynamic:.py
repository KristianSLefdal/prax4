def generete_letter():
    while True:
        for letter in ("abcdefghijklmnopqrstuvwxyzæøå"):
            print(letter)
            yield
bokstav = generete_letter()

x = 0
while x < 29:
    next(bokstav)
    x+= 0