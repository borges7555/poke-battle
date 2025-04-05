from prints import *
from create_defaul_trainers import *
from data_types import *
from battle_calcs import *
from show_pic import *
from chosen_action import *
from opponent_action import *

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
    user_pokemon_down = 0
    opponent_pokemon_down = 0

    pk_in_batlle_user = 0
    pk_in_batlle_opponent = 0

    opponent_speed = opponent[1][pk_in_batlle_opponent][1][5]
    user_speed = trainer[1][pk_in_batlle_user][1][5]
    opponent_hp = opponent[1][pk_in_batlle_opponent][1][0]
    user_hp = trainer[1][pk_in_batlle_user][1][0]

    while not user_pokemon_down == 6 or opponent_pokemon_down == 6:
        if show_picture(opponent[1][pk_in_batlle_opponent][0][0].lower()):
            print(f"HP: {opponent_hp}/{opponent[1][pk_in_batlle_opponent][0][4]}")
        else:
            print(f"Couldn't show picture of {opponent[1][pk_in_batlle_opponent][0][0]}")

        if show_picture(trainer[1][pk_in_batlle_user][0][0].lower()):
            print(f"HP: {user_hp}/{trainer[1][pk_in_batlle_user][0][4]}")
        else:
            print(f"Couldn't show picture of {trainer[1][pk_in_batlle_user][0][0]}")

        print("\nWhat will you do?")
        print("1. Attack")
        print("2. Switch Pokémon")
        print("3. Run")
        action = input()
        while action not in ["1", "2", "3"]:
            print("\nInvalid input. Try again.")
            action = input()
        
        opponent_action = opponent_choose_action(opponent, pk_in_batlle_opponent, trainer, pk_in_batlle_user)
        if action == "3":
            chose_run(trainer, opponent)

        elif opponent_action == "switch" and action == "2":
            pk_in_batlle_opponent = opponent_switch(opponent, pk_in_batlle_opponent, trainer, pk_in_batlle_user)
            opponent_hp = opponent[1][pk_in_batlle_opponent][1][0]
            opponent_speed = opponent[1][pk_in_batlle_opponent][1][5]
            pk_in_batlle_user = chose_switch(trainer, pk_in_batlle_user)
            user_hp = trainer[1][pk_in_batlle_user][1][0]
            user_speed = trainer[1][pk_in_batlle_user][1][5]

        elif opponent_action == "attack" and action == "2":
            pk_in_batlle_user = chose_switch(trainer, pk_in_batlle_user)
            user_hp = trainer[1][pk_in_batlle_user][1][0]
            user_speed = trainer[1][pk_in_batlle_user][1][5]
            #opponent attacks
            user_hp = opponent_attacks(opponent, pk_in_batlle_opponent, trainer, pk_in_batlle_user)
            trainer[1][pk_in_batlle_user][1][0] = user_hp
            #TODO:check if user pokemon is knocked out

        elif opponent_action == "switch" and action == "1":
            pk_in_batlle_opponent = opponent_switch(opponent, pk_in_batlle_opponent, trainer, pk_in_batlle_user)
            opponent_hp = opponent[1][pk_in_batlle_opponent][1][0]
            opponent_speed = opponent[1][pk_in_batlle_opponent][1][5]
            #user attacks
            opponent_hp = chose_attack(trainer, pk_in_batlle_user, opponent, pk_in_batlle_opponent)
            opponent[1][pk_in_batlle_opponent][1][0] = opponent_hp
            #TODO:check if opponent pokemon is knocked out 

        elif opponent_speed >= user_speed:    
            if opponent_action == "attack" and action == "1":
                user_hp = opponent_attacks(opponent, pk_in_batlle_opponent, trainer, pk_in_batlle_user)
                trainer[1][pk_in_batlle_user][1][0] = user_hp
                #TODO:check if user pokemon is knocked out
                opponent_hp = chose_attack(trainer, pk_in_batlle_user, opponent, pk_in_batlle_opponent)
                opponent[1][pk_in_batlle_opponent][1][0] = opponent_hp
                #TODO:check if opponent pokemon is knocked out
        else:
            if opponent_action == "attack" and action == "1":
                opponent_hp = chose_attack(trainer, pk_in_batlle_user, opponent, pk_in_batlle_opponent)
                opponent[1][pk_in_batlle_opponent][1][0] = opponent_hp
                #TODO:check if opponent pokemon is knocked out
                user_hp = opponent_attacks(opponent, pk_in_batlle_opponent, trainer, pk_in_batlle_user)
                trainer[1][pk_in_batlle_user][1][0] = user_hp
                #TODO:check if user pokemon is knocked out

        break

    print(f"\n{trainer[0]} won against {opponent[0]}!")

    return