#In this task I will perform a request for a letter

def generate_a_letter():
    letter = 'a'
    while True:
        yield letter
        if letter == 'e':
            letter = 'a'
        else:
            letter = chr(ord(letter)+ 1)

if __name__ == '__main__':
    #create a generator
    letters = generate_a_letter()

    for i in range(2):
        for j in range(5):
            print(next(letters))
