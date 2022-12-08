#Create a script called GenerateLetter.py. In the script, create a function called generate_letter which is to serve as a generator function. The generator should return a letter in the range a to e. If the generator returns the letter e, it should return the letter a the next time the generator function object is used. Demonstrate the use of the generator in the main portion of your script by display the letters a to e twice.
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
