import time


def print_messages(message):
    print(message)
    time.sleep(3)



def introduction():
    print_messages("Welcome to your adventure! ")
    print_messages("We're going to have a great time,\n"
         "as long as you make the right choice" )
    print_messages("Let's start off easy.")
    name = input("What's your name? ")
    print_messages(f"Hi  {name}, Let's get started! ")


    




def start_game():
    introduction()


start_game()