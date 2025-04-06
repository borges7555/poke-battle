from data_types import *
from battle_calcs import *

def opponent_choose_action(bot_trainer: Trainer, bot_pk_in_battle: int, user_trainer: Trainer, user_pk_in_battle: int) -> str:
    if calc_effectiveness(user_trainer[1][user_pk_in_battle][0][1], bot_trainer[1][bot_pk_in_battle]) >= 2 or calc_effectiveness(user_trainer[1][user_pk_in_battle][0][2], bot_trainer[1][bot_pk_in_battle]) >= 2:
        #switch
        return "switch"
    else:
        #attack
        return "attack"


def opponent_attacks(bot_traner: Trainer, bot_pk_in_battle: int, user_trainer: Trainer, user_pk_in_battle: int) -> int:
    hp_left = 1
    
    return hp_left


def opponent_switch(bot_trainer: Trainer, bot_pk_in_battle: int, user_trainer: Trainer, user_pk_in_battle: int) -> int:
    id = 0
    
    return id