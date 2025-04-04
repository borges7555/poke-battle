from prints import *
from create_defaul_trainers import *
from data_types import *
from battle_calcs import *
from show_pic import *
from chosen_action import *

def game(trainer: Trainer, trainers: list):
    print("\nChoose a trainer to fight against:")
    for i in range(len(trainers)):
        print(f"{i + 1}. {trainers[i][0]}")

    aux = input()
    while not aux.isdigit():
        print("\nInvalid input. Try again.")
        aux = input()

    aux = int(aux)
    while aux < 1 or aux > len(trainers):
        print("\nInvalid input. Try again.")
        aux = int(input())

    opponent = trainers[aux - 1]
    battle_ended = False
    while not battle_ended:
        pk_in_batlle_user = 0
        pk_in_batlle_opponent = 0
        if show_picture(opponent[1][pk_in_batlle_opponent][0][0].lower()):
            #print health bar
            aux = aux
        else:
            print(f"Couldn't show picture of {opponent[1][pk_in_batlle_opponent][0][0]}")

        if show_picture(trainer[1][pk_in_batlle_user][0][0].lower()):
            #print health bar
            aux = aux
        else:
            print(f"Couldn't show picture of {trainer[1][pk_in_batlle_user][0][0]}")

        print("What will you do?")
        print("1. Attack")
        print("2. Switch Pokémon")
        print("3. Run")
        action = input()
        while action not in ["1", "2", "3"]:
            print("\nInvalid input. Try again.")
            action = input()

        if action == "1":
            opponent_hp = chose_attack(trainer, pk_in_batlle_user, opponent, pk_in_batlle_opponent)
            opponent[1][pk_in_batlle_opponent][1] = opponent_hp
            '''
            if opponent[1][pk_in_batlle_opponent][1] == 0:
                #remove pokemon from battle
            '''
        elif action == "2":
            pk_in_batlle_user = chose_switch(trainer, pk_in_batlle_user)
        elif action == "3":
            chose_run(trainer, opponent)

        break

    return