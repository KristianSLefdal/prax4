def letter_generator():
    while True:
        for letter in ("abcdefghijklmnopqrstuvwxyzæøå"):
            print (letter)
            yield
    
bokstav = letter_generator()

x= 0
while x < 29:
    next(bokstav)
    x += 1