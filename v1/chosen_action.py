import sys
from data_types import *
from battle_calcs import *

def chose_attack(trainer: Trainer, pk_in_battle_user: int, opponent: Trainer, pk_in_battle_opponent: int) -> int:
    print("\nChoose an attack:")
    for i in range(4):
        print(f"{i + 1}. {trainer[1][pk_in_battle_user][i+2][0]}")

    attack = input()
    while attack not in ["1", "2", "3", "4"]:
        print("\nInvalid input. Try again.")
        attack = input()
    
    chosen_move = trainer[1][pk_in_battle_user][int(attack)+1]
    damage = calc_damage(trainer[1][pk_in_battle_user], opponent[1][pk_in_battle_opponent], chosen_move)
    print(f"\n{trainer[1][pk_in_battle_user][0][0]}'s {chosen_move[0]} dealt {damage} damage to {opponent[1][pk_in_battle_opponent][0][0]}.")
    if opponent[1][pk_in_battle_opponent][1][0] - damage < 0:
        return 0
    
    return opponent[1][pk_in_battle_opponent][1] - damage


def chose_switch(trainer: Trainer, pk_in_battle_user: int) -> int:
    id = ""
    valid_ids = []
    i = 0
    print("\nChoose a Pokémon to switch to:")
    for pokemon in trainer[1][:pk_in_battle_user]+trainer[1][pk_in_battle_user+1:]:#TODO: fix bug when pk_in_battle_user is 5
        i += 1
        valid_ids.append(str(i))
        print(f"{str(i)}. {pokemon[0][0]}")
        for move in pokemon[1:]:
            print(f"    - {move[0]}")

    id = input()
    
    while id not in valid_ids:
        print("\nInvalid input. Try again.")
        id = input

    return (int(id)-1)
    

def chose_run(trainer: Trainer, opponent: Trainer):
    print("\nYou ran away.")
    print(f"{trainer[0]} lost to {opponent[0]}.")
    sys.exit(1)
        