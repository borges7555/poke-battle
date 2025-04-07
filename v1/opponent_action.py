from data_types import *
from battle_calcs import *

def opponent_choose_action(bot_trainer: Trainer, bot_pk_in_battle: int, user_trainer: Trainer, user_pk_in_battle: int) -> str:
    if calc_effectiveness(user_trainer[1][user_pk_in_battle][0][1], bot_trainer[1][bot_pk_in_battle]) >= 2 or calc_effectiveness(user_trainer[1][user_pk_in_battle][0][2], bot_trainer[1][bot_pk_in_battle]) >= 2:
        #switch
        return "switch"
    else:
        #attack
        return "attack"

def opponent_choose_attack(bot_trainer: Trainer, bot_pk_in_battle: int, user_trainer: Trainer, user_pk_in_battle: int) -> TM: #TODO:
    bot_chosen_tm = bot_trainer[1][bot_pk_in_battle][1]
    
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