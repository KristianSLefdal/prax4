from time import *
import random

number_selected_random = random.randint(0,10)
attempts = 10

message = ''

begin = time()
gamebegin = localtime(begin)

while attempts > 0:

    user_selection = int(input('enter number: '))
    if user_selection == number_selected_random:
        print("You won the game")
        break
    elif number_selected_random > user_selection:
        print("is greater")
    else:
        print("is lower")

end = time()
timedifference = end - begin

print(timedifference)






