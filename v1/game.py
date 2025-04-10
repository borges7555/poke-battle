import random
from prints import *
from create_defaul_trainers import *
from data_types import *
from battle_calcs import *
from show_pic import *
from chosen_action import *
from opponent_action import *
import time

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
    kos_to_win = 4 #TODO: change to 6

    pk_in_batlle_user = 0
    pk_in_batlle_opponent = random.randint(0, 5)

    opponent_speed = opponent[1][pk_in_batlle_opponent][1][5]
    user_speed = trainer[1][pk_in_batlle_user][1][5]
    opponent_hp = opponent[1][pk_in_batlle_opponent][1][0]
    user_hp = trainer[1][pk_in_batlle_user][1][0]

    print(f"\n{opponent[0]} sent out {opponent[1][pk_in_batlle_opponent][0][0]}.")
    time.sleep(1)
    print(f"{trainer[0]} sent out {trainer[1][pk_in_batlle_user][0][0]}.")
    time.sleep(1)
    while user_pokemon_down != kos_to_win and opponent_pokemon_down != kos_to_win:
        print_pokemons_in_battle(trainer, pk_in_batlle_user, user_hp, opponent, pk_in_batlle_opponent, opponent_hp)
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
            user_run(trainer, opponent)

        elif opponent_action == "switch" and action == "2":
            aux = pk_in_batlle_user
            pk_in_batlle_user = user_switch(trainer, pk_in_batlle_user)
            if pk_in_batlle_user == None:
                pk_in_batlle_user = aux
                continue
            #opponent switches
            time.sleep(1)
            print(f"\n{opponent[0]} retrieved {opponent[1][pk_in_batlle_opponent][0][0]}.")
            pk_in_batlle_opponent = opponent_switch(opponent, pk_in_batlle_opponent, trainer, aux)
            opponent_hp = opponent[1][pk_in_batlle_opponent][1][0]
            opponent_speed = opponent[1][pk_in_batlle_opponent][1][5]
            time.sleep(1)
            print(f"{opponent[0]} sent out {opponent[1][pk_in_batlle_opponent][0][0]}.")
            #user switches
            time.sleep(1)
            print(f"\n{trainer[0]} retrieved {trainer[1][aux][0][0]}.")
            user_hp = trainer[1][pk_in_batlle_user][1][0]
            user_speed = trainer[1][pk_in_batlle_user][1][5]
            time.sleep(1)
            print(f"{trainer[0]} sent out {trainer[1][pk_in_batlle_user][0][0]}.")

        elif opponent_action == "attack" and action == "2":
            aux = pk_in_batlle_user
            pk_in_batlle_user = user_switch(trainer, pk_in_batlle_user)
            if pk_in_batlle_user == None:
                pk_in_batlle_user = aux
                continue
            #opponent chooses move
            opponent_chosen_tm = opponent_choose_attack(opponent, pk_in_batlle_opponent, trainer, aux)
            #user switches
            print(f"\n{trainer[0]} retrieved {trainer[1][aux][0][0]}.")
            user_hp = trainer[1][pk_in_batlle_user][1][0]
            user_speed = trainer[1][pk_in_batlle_user][1][5]
            time.sleep(1)
            print(f"\n{trainer[0]} sent out {trainer[1][pk_in_batlle_user][0][0]}.")
            time.sleep(1)
            print_pokemons_in_battle(trainer, pk_in_batlle_user, user_hp, opponent, pk_in_batlle_opponent, opponent_hp)
            #opponent attacks
            user_hp = opponent_attacks(opponent, pk_in_batlle_opponent, opponent_chosen_tm, trainer, pk_in_batlle_user)
            trainer[1][pk_in_batlle_user][1][0] = user_hp
            #check if user pokemon is knocked out
            if user_hp == 0:
                time.sleep(1)
                print(f"\n{trainer[0]}'s {trainer[1][pk_in_batlle_user][0][0]} fainted.")
                user_pokemon_down += 1
                if user_pokemon_down != kos_to_win:
                    pk_in_batlle_user = user_switch(trainer, pk_in_batlle_user, False)
                    user_hp = trainer[1][pk_in_batlle_user][1][0]
                    user_speed = trainer[1][pk_in_batlle_user][1][5]      
                    time.sleep(1)
                    print(f"{trainer[0]} sent out {trainer[1][pk_in_batlle_user][0][0]}.")

        elif opponent_action == "switch" and action == "1":
            #user chooses move
            user_chosen_tm = user_choose_attack(trainer, pk_in_batlle_user)
            if user_chosen_tm == None:
                continue
            #opponent switches
            time.sleep(1)
            print(f"\n{opponent[0]} retrieved {opponent[1][pk_in_batlle_opponent][0][0]}.")
            pk_in_batlle_opponent = opponent_switch(opponent, pk_in_batlle_opponent, trainer, pk_in_batlle_user)
            opponent_hp = opponent[1][pk_in_batlle_opponent][1][0]
            opponent_speed = opponent[1][pk_in_batlle_opponent][1][5]
            time.sleep(1)
            print(f"{opponent[0]} sent out {opponent[1][pk_in_batlle_opponent][0][0]}.")
            time.sleep(1)
            print_pokemons_in_battle(trainer, pk_in_batlle_user, user_hp, opponent, pk_in_batlle_opponent, opponent_hp)
            #user attacks
            opponent_hp = user_attacks(trainer, pk_in_batlle_user, user_chosen_tm, opponent, pk_in_batlle_opponent)
            opponent[1][pk_in_batlle_opponent][1][0] = opponent_hp
            #check if opponent pokemon is knocked out 
            if opponent_hp == 0:
                time.sleep(1)
                print(f"\n{opponent[0]}'s {opponent[1][pk_in_batlle_opponent][0][0]} fainted.")
                opponent_pokemon_down += 1
                if opponent_pokemon_down != kos_to_win:
                    pk_in_batlle_opponent = opponent_switch(opponent, pk_in_batlle_opponent, trainer, pk_in_batlle_user)
                    opponent_hp = opponent[1][pk_in_batlle_opponent][1][0]
                    opponent_speed = opponent[1][pk_in_batlle_opponent][1][5]
                    time.sleep(1)
                    print(f"{opponent[0]} sent out {opponent[1][pk_in_batlle_opponent][0][0]}.")

        elif opponent_speed >= user_speed:    
            if opponent_action == "attack" and action == "1":
                user_chosen_tm = user_choose_attack(trainer, pk_in_batlle_user)
                if user_chosen_tm == None:
                    continue
                #opponent attacks
                opponent_chosen_tm = opponent_choose_attack(opponent, pk_in_batlle_opponent, trainer, pk_in_batlle_user)
                user_hp = opponent_attacks(opponent, pk_in_batlle_opponent, opponent_chosen_tm, trainer, pk_in_batlle_user)
                trainer[1][pk_in_batlle_user][1][0] = user_hp
                #check if user pokemon is knocked out
                if user_hp == 0:
                    time.sleep(1)
                    print(f"\n{trainer[0]}'s {trainer[1][pk_in_batlle_user][0][0]} fainted.")
                    user_pokemon_down += 1
                    if user_pokemon_down != kos_to_win:
                        pk_in_batlle_user = user_switch(trainer, pk_in_batlle_user, False)
                        user_hp = trainer[1][pk_in_batlle_user][1][0]
                        user_speed = trainer[1][pk_in_batlle_user][1][5]
                        time.sleep(1)
                        print(f"{trainer[0]} sent out {trainer[1][pk_in_batlle_user][0][0]}.")
                else:
                    #user attacks if pokemon wasnt knocked out
                    time.sleep(1)
                    opponent_hp = user_attacks(trainer, pk_in_batlle_user, user_chosen_tm, opponent, pk_in_batlle_opponent)
                    opponent[1][pk_in_batlle_opponent][1][0] = opponent_hp
                    #check if opponent pokemon is knocked out
                    if opponent_hp == 0:
                        time.sleep(1)
                        print(f"\n{opponent[0]}'s {opponent[1][pk_in_batlle_opponent][0][0]} fainted.")
                        opponent_pokemon_down += 1
                        if opponent_pokemon_down != kos_to_win:
                            pk_in_batlle_opponent = opponent_switch(opponent, pk_in_batlle_opponent, trainer, pk_in_batlle_user)
                            opponent_hp = opponent[1][pk_in_batlle_opponent][1][0]
                            opponent_speed = opponent[1][pk_in_batlle_opponent][1][5]
                            time.sleep(1)
                            print(f"{opponent[0]} sent out {opponent[1][pk_in_batlle_opponent][0][0]}.")
        else:
            if opponent_action == "attack" and action == "1":
                #user attacks
                user_chosen_tm = user_choose_attack(trainer, pk_in_batlle_user)
                if user_chosen_tm == None:
                    continue
                opponent_hp = user_attacks(trainer, pk_in_batlle_user, user_chosen_tm, opponent, pk_in_batlle_opponent)
                opponent[1][pk_in_batlle_opponent][1][0] = opponent_hp
                #check if opponent pokemon is knocked out
                if opponent_hp == 0:
                    time.sleep(1)
                    print(f"\n{opponent[0]}'s {opponent[1][pk_in_batlle_opponent][0][0]} fainted.")
                    opponent_pokemon_down += 1
                    if opponent_pokemon_down != kos_to_win:
                        pk_in_batlle_opponent = opponent_switch(opponent, pk_in_batlle_opponent, trainer, pk_in_batlle_user)
                        opponent_hp = opponent[1][pk_in_batlle_opponent][1][0]
                        opponent_speed = opponent[1][pk_in_batlle_opponent][1][5]
                        time.sleep(1)
                        print(f"{opponent[0]} sent out {opponent[1][pk_in_batlle_opponent][0][0]}.")
                else:
                    #opponent attacks if pokemon wasnt knocked out
                    opponent_chosen_tm = opponent_choose_attack(opponent, pk_in_batlle_opponent, trainer, pk_in_batlle_user)
                    time.sleep(1)
                    user_hp = opponent_attacks(opponent, pk_in_batlle_opponent, opponent_chosen_tm, trainer, pk_in_batlle_user)
                    trainer[1][pk_in_batlle_user][1][0] = user_hp
                    #check if user pokemon is knocked out
                    if user_hp == 0:
                        time.sleep(1)
                        print(f"\n{trainer[0]}'s {trainer[1][pk_in_batlle_user][0][0]} fainted.")
                        user_pokemon_down += 1
                        if user_pokemon_down != kos_to_win:
                            pk_in_batlle_user = user_switch(trainer, pk_in_batlle_user, False)
                            user_hp = trainer[1][pk_in_batlle_user][1][0]
                            user_speed = trainer[1][pk_in_batlle_user][1][5]
                            time.sleep(1)
                            print(f"{trainer[0]} sent out {trainer[1][pk_in_batlle_user][0][0]}.")

        time.sleep(1)

    if user_pokemon_down == kos_to_win:
        print(f"\n{opponent[0]} won against {trainer[0]}!")
    else:
        print(f"\n{trainer[0]} won against {opponent[0]}!")

    return