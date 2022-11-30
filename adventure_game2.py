import time
import random

def print_messages(message):
    print(message)
    time.sleep(2.5)



def introduction():
    print_messages("Welcome to your adventure! ")
    print_messages("We're going to have a great time,\n"
         "as long as you make the right choice" )
    print_messages("Let's start off easy.")
    name = input("What's your name? ")
    print_messages(f"Hi {name}, Let's get started! ")


def valid_answer(answer, option1, option2):
    while True:
        response = input(answer).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_messages("Sorry, that's not an option.")
    return response


def begin_adventure():
    random_setting = ["dark", "wet", "cursed", "scary"]
    response = valid_answer("You wake up in a " + random.choice(random_setting) + " forest, not sure how you got there."
        " Do you STAY where you are or do you EXPLORE?\n",
         "explore", "stay" )
    if "stay" in response:
        print_messages("Uh oh! You've been eaten by a monster :( ")
    elif "explore" in response:
        print_messages("Wow! You've come across a pot of gold with a map home! Congrats :) ")

    


def play_again():
    response = valid_answer("Do you want to play again?\n ", "yes", "no")
    if "yes" in response:
        print_messages("Great, let's go! ")
        begin_adventure()
    elif "no" in response:
        print_messages("Ok, have a great day. ")


def start_game():
    introduction()
    begin_adventure()
    play_again()


start_game()