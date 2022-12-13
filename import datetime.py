from datetime import *
from time import *
import random


def creat_time():
    now = datetime.today()
    return now

def output_local_time(now):
    print(f"{now.hour}:{now.minute}:{now.second}")

def calculate_difference(endtime, starttime):
    difference = starttime - endtime
    return difference

def generate_random(maximum):
    number = random.randint(0,maximum)
    return number

time01 = creat_time()

output_local_time(time01)

input("press enter")

time02 = creat_time()

differenceintime = calculate_difference(time01, time02)
print("the time difference is:", differenceintime, "seconds")

input("press enter to continue")

maxi = 245
anumber = generate_random(maxi)
print(anumber)

