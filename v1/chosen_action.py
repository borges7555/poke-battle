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
    
    chosen_move = trainer[1][pk_in_battle_user][int(attack)]
    damage = calc_damage(trainer[1][pk_in_battle_user], opponent[1][pk_in_battle_opponent], chosen_move)
    print(f"{chosen_move[0]} dealt {damage} damage to {opponent[1][pk_in_battle_opponent][0][0]}.")
    if opponent[1][pk_in_battle_opponent][1] - damage < 0:
        return 0
    
    return opponent[1][pk_in_battle_opponent][1] - damage


def chose_switch(trainer: Trainer, pk_in_battle_user: int) -> int:
    print("\nChoose a Pokémon to switch to:")
    


def chose_run(trainer: Trainer, opponent: Trainer):
    print("\nYou ran away.")
    print(f"{trainer[0]} lost to {opponent[0]}.")
    sys.exit(1)
        