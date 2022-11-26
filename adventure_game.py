import time

intro = print("Welcome to your adventure! ")
time.sleep(1)

name = input("What's your name? ")
print("Hi " + name + ", Let's get started! ")
time.sleep(2)

begin = input("You wake up in a dark forest, not sure how you got there. Do you STAY where you are or do you EXPLORE? ")
time.sleep(2)

if begin == "EXPLORE":
    print("Good choice! Let's get going ")
    act1 = input("You start exploring and you come across a path. Do you turn LEFT towards the meadow or RIGHT towards the river? ")
else: 
    print("Uh Oh! You've been eaten by a monster! ")    
    quit()

time.sleep(2)
