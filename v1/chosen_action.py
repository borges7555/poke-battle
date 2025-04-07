import sys
from data_types import *
from battle_calcs import *

def user_choose_attack(trainer: Trainer, pk_in_battle_user: int) -> TM:
    print("\nChoose a move:")
    for i in range(4):
        print(f"{i + 1}. {trainer[1][pk_in_battle_user][i+2][0]}")

    attack = input()
    while attack not in ["1", "2", "3", "4"]:
        print("\nInvalid input. Try again.")
        attack = input()
    
    chosen_move = trainer[1][pk_in_battle_user][int(attack)+1]
    return chosen_move


def user_attacks(trainer: Trainer, pk_in_battle_user: int, chosen_move: TM, opponent: Trainer, pk_in_battle_opponent: int) -> int:
    print(f"\n{trainer[1][pk_in_battle_user][0][0]} used {chosen_move[0]}.")
    damage = calc_damage(trainer[1][pk_in_battle_user], opponent[1][pk_in_battle_opponent], chosen_move)
    print(f"It did {damage} damage.")
    if opponent[1][pk_in_battle_opponent][1][0] - damage < 0:
        return 0
    
    return opponent[1][pk_in_battle_opponent][1][0] - damage


def user_switch(trainer: Trainer, pk_in_battle_user: int) -> int:
    pokemon_hp = 0
    print("\nChoose a Pokémon to switch to:")
    while pokemon_hp == 0:
        valid_ids = []
        i = 0
        aux1 = trainer[1][:pk_in_battle_user] + trainer[1][pk_in_battle_user + 1:] if pk_in_battle_user != 5 else trainer[1][:-1]
        for pokemon in aux1:
            i += 1
            valid_ids.append(str(i))
            print(f"{str(i)}. {pokemon[0][0]}")
            for move in pokemon[2:]:
                print(f"    - {move[0]}")

        aux2 = input()
        
        while aux2 not in valid_ids:
            print("\nInvalid input. Try again.")
            aux2 = input()

        id = int(aux2)-1 if int(aux2)-1 < pk_in_battle_user else int(aux2)
        pokemon_hp = trainer[1][id][1][0]
        if pokemon_hp == 0:
            print("\nThis Pokémon is fainted. Choose another one.")

    return id
    

def user_run(trainer: Trainer, opponent: Trainer):
    print("\nYou ran away.")
    print(f"{trainer[0]} lost to {opponent[0]}.")
    sys.exit(1)
        