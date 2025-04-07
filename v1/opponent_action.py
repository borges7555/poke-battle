from data_types import *
from battle_calcs import *

def opponent_choose_action(bot_trainer: Trainer, bot_pk_in_battle: int, user_trainer: Trainer, user_pk_in_battle: int) -> str:
    #if user hits for super effective
    if calc_effectiveness(user_trainer[1][user_pk_in_battle][0][1], bot_trainer[1][bot_pk_in_battle]) >= 2 or calc_effectiveness(user_trainer[1][user_pk_in_battle][0][2], bot_trainer[1][bot_pk_in_battle]) >= 2:
        return "switch"

    #se todos os ataques do pokemon forem not very effective, switch
    for i in range(1, 4):
        if calc_effectiveness(bot_trainer[1][bot_pk_in_battle][i][1], user_trainer[1][user_pk_in_battle]) >= 1:
            aux = False
            break
        else:
            aux = True

    if aux:
        return "switch"

    return "attack"


def opponent_choose_attack(bot_trainer: Trainer, bot_pk_in_battle: int, user_trainer: Trainer, user_pk_in_battle: int) -> TM: #TODO:
    aux = 0
    for i in range(1, 4):
        if calc_damage(bot_trainer[1][bot_pk_in_battle], user_trainer[1][user_pk_in_battle], bot_trainer[1][bot_pk_in_battle][i]) > aux:
            bot_chosen_tm = bot_trainer[1][bot_pk_in_battle][i]
            aux = calc_damage(bot_trainer[1][bot_pk_in_battle], user_trainer[1][user_pk_in_battle], bot_trainer[1][bot_pk_in_battle][i])

    return bot_chosen_tm


def opponent_attacks(bot_trainer: Trainer, bot_pk_in_battle: int, bot_chosen_tm: TM, user_trainer: Trainer, user_pk_in_battle: int) -> int:
    print(f"\n{bot_trainer[1][bot_pk_in_battle][0][0]} used {bot_chosen_tm[0]}.")
    damage = calc_damage(bot_trainer[1][bot_pk_in_battle], user_trainer[1][user_pk_in_battle], bot_chosen_tm)
    print(f"\nIt did {damage} damage.")
    if user_trainer[1][user_pk_in_battle][1][0] - damage < 0:
        return 0
    
    return user_trainer[1][user_pk_in_battle][1][0] - damage


def opponent_switch(bot_trainer: Trainer, bot_pk_in_battle: int, user_trainer: Trainer, user_pk_in_battle: int) -> int: #TODO:
    id = 0
    
    return id