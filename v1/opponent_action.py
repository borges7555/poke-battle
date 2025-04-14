from data_types import *
from battle_calcs import *
import time

def opponent_choose_action(bot_trainer: Trainer, bot_pk_in_battle: int, user_trainer: Trainer, user_pk_in_battle: int) -> str:
    if len(bot_trainer[1]) == 1:
        return "attack"
    
    #if nuber of pokemons alive is 1, attack
    num = 0
    for i in range(0, len(bot_trainer[1])):
        if bot_trainer[1][i][1][0] > 0:
            num += 1

    if num == 1:
        return "attack"
    
    #if all bot pokemons take super effective damage from user, attack
    for i in range(0, len(bot_trainer[1])):
        if bot_trainer[1][i][1][0] > 0:
            if calc_effectiveness(user_trainer[1][user_pk_in_battle][0][1], bot_trainer[1][i]) >= 2 or calc_effectiveness(user_trainer[1][user_pk_in_battle][0][2], bot_trainer[1][i]) >= 2:
                aux = True
            else:
                aux = False
                break
                
    if aux:
        return "attack"

    #if user hits for super effective
    if calc_effectiveness(user_trainer[1][user_pk_in_battle][0][1], bot_trainer[1][bot_pk_in_battle]) >= 2 or calc_effectiveness(user_trainer[1][user_pk_in_battle][0][2], bot_trainer[1][bot_pk_in_battle]) >= 2:
        #if bot also hits for super effective
        if calc_effectiveness(bot_trainer[1][bot_pk_in_battle][0][1], user_trainer[1][user_pk_in_battle]) >= 2 or calc_effectiveness(bot_trainer[1][bot_pk_in_battle][0][2], user_trainer[1][user_pk_in_battle]) >= 2:
            #if bot is faster
            if bot_trainer[1][bot_pk_in_battle][1][5] >= user_trainer[1][user_pk_in_battle][1][5]:
                return "attack"
            
        return "switch"
    
    #if bot has move super effective against user
    for k in range(2, 6):
        if calc_effectiveness(bot_trainer[1][bot_pk_in_battle][k][1], user_trainer[1][user_pk_in_battle]) >= 2:
            return "attack"

    #se bot tiver algum pokemon que seja effective contra pokemon do user
    for i in range(0, len(bot_trainer[1])):
        if bot_trainer[1][i][1][0] > 0:
            if calc_effectiveness(bot_trainer[1][i][0][1], user_trainer[1][user_pk_in_battle]) >= 2 or calc_effectiveness(bot_trainer[1][i][0][2], user_trainer[1][user_pk_in_battle]) >= 2:
                if calc_effectiveness(user_trainer[1][user_pk_in_battle][0][1], bot_trainer[1][i]) <= 1 and calc_effectiveness(user_trainer[1][user_pk_in_battle][0][2], bot_trainer[1][i]) <= 1:
                    if i != bot_pk_in_battle:
                        if not share_weaknesses(bot_trainer[1][i], bot_trainer[1][bot_pk_in_battle]):
                            return "switch"
                    else:
                        return "attack"
            else:
                for k in range(2, 6):
                    if calc_effectiveness(bot_trainer[1][i][k][1], user_trainer[1][user_pk_in_battle]) == 4:
                        if calc_effectiveness(user_trainer[1][user_pk_in_battle][0][1], bot_trainer[1][i]) <= 1 and calc_effectiveness(user_trainer[1][user_pk_in_battle][0][2], bot_trainer[1][i]) <= 1:
                            if i != bot_pk_in_battle:
                                if not share_weaknesses(bot_trainer[1][i], bot_trainer[1][bot_pk_in_battle]):
                                    return "switch"
                            else:
                                return "attack"

    #se todos os ataques do pokemon forem not very effective, switch
    for i in range(2, 6):
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
    for i in range(2, 6):
        if bot_calc_damage(bot_trainer[1][bot_pk_in_battle], user_trainer[1][user_pk_in_battle], bot_trainer[1][bot_pk_in_battle][i], False) > aux:
            bot_chosen_tm = bot_trainer[1][bot_pk_in_battle][i]
            aux = bot_calc_damage(bot_trainer[1][bot_pk_in_battle], user_trainer[1][user_pk_in_battle], bot_trainer[1][bot_pk_in_battle][i], False)

    return bot_chosen_tm


def opponent_attacks(bot_trainer: Trainer, bot_pk_in_battle: int, bot_chosen_tm: TM, user_trainer: Trainer, user_pk_in_battle: int) -> int:
    print(f"\n{bot_trainer[1][bot_pk_in_battle][0][0]} used {bot_chosen_tm[0]}.")
    damage = bot_calc_damage(bot_trainer[1][bot_pk_in_battle], user_trainer[1][user_pk_in_battle], bot_chosen_tm, True)
    time.sleep(1)
    print(f"It did {damage} damage.")
    if user_trainer[1][user_pk_in_battle][1][0] - damage < 0:
        return 0
    
    return user_trainer[1][user_pk_in_battle][1][0] - damage


def opponent_switch(bot_trainer: Trainer, bot_pk_in_battle: int, user_trainer: Trainer, user_pk_in_battle: int) -> int: #TODO:
    #se bot tiver algum pokemon que seja effective contra pokemon do user
    for id in range(0, len(bot_trainer[1])):
        if id != bot_pk_in_battle and bot_trainer[1][id][1][0] > 0:
            if calc_effectiveness(bot_trainer[1][id][0][1], user_trainer[1][user_pk_in_battle]) >= 2 or calc_effectiveness(bot_trainer[1][id][0][2], user_trainer[1][user_pk_in_battle]) >= 2:
                if calc_effectiveness(user_trainer[1][user_pk_in_battle][0][1], bot_trainer[1][id]) <= 1 and calc_effectiveness(user_trainer[1][user_pk_in_battle][0][2], bot_trainer[1][id]) <= 1:
                    #print("#Debug: pokemon que tem tipo super efetivo")
                    if not share_weaknesses(bot_trainer[1][id], bot_trainer[1][bot_pk_in_battle]):
                        return id
            else:
                for k in range(2, 6):
                    if calc_effectiveness(bot_trainer[1][id][k][1], user_trainer[1][user_pk_in_battle]) == 4:
                        if calc_effectiveness(user_trainer[1][user_pk_in_battle][0][1], bot_trainer[1][id]) <= 1 and calc_effectiveness(user_trainer[1][user_pk_in_battle][0][2], bot_trainer[1][id]) <= 1:
                            #print("#Debug: pokemon que tem ataque 4x efetivo")
                            if not share_weaknesses(bot_trainer[1][id], bot_trainer[1][bot_pk_in_battle]):
                                return id
    
    #se tiver pokemon que resista ao pokemon do user
    for id in range(0, len(bot_trainer[1])):
        if id != bot_pk_in_battle and bot_trainer[1][id][1][0] > 0:
            if (calc_effectiveness(user_trainer[1][user_pk_in_battle][0][1], bot_trainer[1][id]) < 1 and calc_effectiveness(user_trainer[1][user_pk_in_battle][0][2], bot_trainer[1][id]) <= 1) or (calc_effectiveness(user_trainer[1][user_pk_in_battle][0][1], bot_trainer[1][id]) <= 1 and calc_effectiveness(user_trainer[1][user_pk_in_battle][0][2], bot_trainer[1][id]) < 1):
                for k in range(2, 6):
                    if calc_effectiveness(bot_trainer[1][id][k][1], user_trainer[1][user_pk_in_battle]) >= 1:
                        aux = False
                        break
                    else:
                        aux = True

                if not aux:
                    #print("#Debug: pokemon que resiste")
                    if not share_weaknesses(bot_trainer[1][id], bot_trainer[1][bot_pk_in_battle]):
                        return id

    #se tiver pokemon que e neutro ao pokemon do user
    for id in range(0, len(bot_trainer[1])):
        if id != bot_pk_in_battle and bot_trainer[1][id][1][0] > 0:
            if calc_effectiveness(user_trainer[1][user_pk_in_battle][0][1], bot_trainer[1][id]) <= 1 and calc_effectiveness(user_trainer[1][user_pk_in_battle][0][2], bot_trainer[1][id]) <= 1:
                for k in range(2, 6):
                    if calc_effectiveness(bot_trainer[1][id][k][1], user_trainer[1][user_pk_in_battle]) >= 2:
                        aux = False
                        break
                    else:
                        aux = True

                if not aux:
                    #print("#Debug: pokemon que e neutro e tem ataque 2x efetivo")
                    if not share_weaknesses(bot_trainer[1][id], bot_trainer[1][bot_pk_in_battle]):
                        return id
                    
                for k in range(2, 6):
                    if calc_effectiveness(bot_trainer[1][id][k][1], user_trainer[1][user_pk_in_battle]) >= 1:
                        aux = False
                        break
                    else:
                        aux = True

                if not aux:
                    #print("#Debug: pokemon que e neutro")
                    if not share_weaknesses(bot_trainer[1][id], bot_trainer[1][bot_pk_in_battle]):
                        return id
                        
    #se tiver pokemon com ataque 2x efetivo
    for id in range(0, len(bot_trainer[1])):
        if id != bot_pk_in_battle and bot_trainer[1][id][1][0] > 0:
            for k in range(2, 6):
                if calc_effectiveness(bot_trainer[1][id][k][1], user_trainer[1][user_pk_in_battle]) >= 2:
                    if calc_effectiveness(user_trainer[1][user_pk_in_battle][0][1], bot_trainer[1][id]) <= 1 and calc_effectiveness(user_trainer[1][user_pk_in_battle][0][2], bot_trainer[1][id]) <= 1:
                        #print("#Debug: pokemon que tem ataque 2x efetivo")
                        if not share_weaknesses(bot_trainer[1][id], bot_trainer[1][bot_pk_in_battle]):
                            return id

    id = random.randint(0, len(bot_trainer[1]) - 1)
    while id == bot_pk_in_battle or bot_trainer[1][id][1][0] == 0: 
        id = random.randint(0, len(bot_trainer[1]) - 1)

    #print("#Debug: pokemon random")
    return id