import random
import time
from data_types import *
from returns import *

def calc_effectiveness(type: str, target: TrainedPokemon) -> float:
    mult = 1
    target_types = [target[0][1], target[0][2]]
    if type == "Normal":
        if "Rock" in target_types:
            mult *= 0.5
        if "Steel" in target_types:
            mult *= 0.5
        if "Ghost" in target_types:
            mult *= 0

    elif type == "Fire":
        if "Grass" in target_types:
            mult *= 2
        if "Water" in target_types:
            mult *= 0.5
        if "Rock" in target_types:
            mult *= 0.5
        if "Bug" in target_types:
            mult *= 2
        if "Steel" in target_types:
            mult *= 2
        if "Dragon" in target_types:
            mult *= 0.5
        if "Fire" in target_types:
            mult *= 0.5
        if "Ice" in target_types:
            mult *= 2

    elif type == "Water":
        if "Fire" in target_types:
            mult *= 2
        if "Water" in target_types:
            mult *= 0.5
        if "Grass" in target_types:
            mult *= 0.5
        if "Ground" in target_types:
            mult *= 2
        if "Rock" in target_types:
            mult *= 2
        if "Dragon" in target_types:
            mult *= 0.5

    elif type == "Electric":
        if "Water" in target_types:
            mult *= 2
        if "Electric" in target_types:
            mult *= 0.5
        if "Ground" in target_types:
            mult *= 0
        if "Flying" in target_types:
            mult *= 2
        if "Dragon" in target_types:
            mult *= 0.5
        if "Grass" in target_types:
            mult *= 0.5

    elif type == "Grass":
        if "Water" in target_types:
            mult *= 2
        if "Grass" in target_types:
            mult *= 0.5
        if "Ground" in target_types:
            mult *= 2
        if "Rock" in target_types:
            mult *= 2
        if "Flying" in target_types:
            mult *= 0.5
        if "Bug" in target_types:
            mult *= 0.5
        if "Fire" in target_types:
            mult *= 0.5
        if "Dragon" in target_types:
            mult *= 0.5
        if "Poison" in target_types:
            mult *= 0.5
        if "Steel" in target_types:
            mult *= 0.5

    elif type == "Ice":
        if "Grass" in target_types:
            mult *= 2
        if "Ice" in target_types:
            mult *= 0.5
        if "Ground" in target_types:
            mult *= 2
        if "Flying" in target_types:
            mult *= 2
        if "Dragon" in target_types:
            mult *= 2
        if "Steel" in target_types:
            mult *= 0.5
        if "Fire" in target_types:
            mult *= 0.5
        if "Water" in target_types:
            mult *= 0.5

    elif type == "Fighting":
        if "Normal" in target_types:
            mult *= 2
        if "Rock" in target_types:
            mult *= 2
        if "Steel" in target_types:
            mult *= 2
        if "Ice" in target_types:
            mult *= 2
        if "Bug" in target_types:
            mult *= 0.5
        if "Ghost" in target_types:
            mult *= 0
        if "Dark" in target_types:
            mult *= 2
        if "Fairy" in target_types:
            mult *= 0.5
        if "Flying" in target_types:
            mult *= 0.5
        if "Psychic" in target_types:
            mult *= 0.5
        if "Poison" in target_types:
            mult *= 0.5

    elif type == "Poison":
        if "Grass" in target_types:
            mult *= 2
        if "Poison" in target_types:
            mult *= 0.5
        if "Fairy" in target_types:
            mult *= 2
        if "Rock" in target_types:
            mult *= 0.5
        if "Ghost" in target_types:
            mult *= 0.5
        if "Steel" in target_types:
            mult *= 0
        if "Ground" in target_types:
            mult *= 0.5

    elif type == "Ground":
        if "Electric" in target_types:
            mult *= 2
        if "Rock" in target_types:
            mult *= 2
        if "Steel" in target_types:
            mult *= 2
        if "Grass" in target_types:
            mult *= 0.5
        if "Flying" in target_types:
            mult *= 0
        if "Bug" in target_types:
            mult *= 0.5
        if "Poison" in target_types:
            mult *= 2
        if "Fire" in target_types:
            mult *= 2

    elif type == "Flying":
        if "Grass" in target_types:
            mult *= 2
        if "Steel" in target_types:
            mult *= 0.5
        if "Bug" in target_types:
            mult *= 2
        if "Fighting" in target_types:
            mult *= 2
        if "Rock" in target_types:
            mult *= 0.5
        if "Electric" in target_types:
            mult *= 0.5

    elif type == "Psychic":
        if "Fighting" in target_types:
            mult *= 2
        if "Psychic" in target_types:
            mult *= 0.5
        if "Poison" in target_types:
            mult *= 2
        if "Steel" in target_types:
            mult *= 0.5
        if "Dark" in target_types:
            mult *= 0

    elif type == "Bug":
        if "Grass" in target_types:
            mult *= 2
        if "Psychic" in target_types:
            mult *= 2
        if "Dark" in target_types:
            mult *= 2
        if "Bug" in target_types:
            mult *= 0.5
        if "Fighting" in target_types:
            mult *= 0.5
        if "Flying" in target_types:
            mult *= 0.5
        if "Ghost" in target_types:
            mult *= 0.5
        if "Poison" in target_types:
            mult *= 0.5
        if "Fairy" in target_types:
            mult *= 0.5
        if "Fire" in target_types:
            mult *= 0.5
        if "Steel" in target_types:
            mult *= 0.5

    elif type == "Rock":
        if "Fire" in target_types:
            mult *= 2
        if "Flying" in target_types:
            mult *= 2
        if "Bug" in target_types:
            mult *= 2
        if "Rock" in target_types:
            mult *= 0.5
        if "Steel" in target_types:
            mult *= 0.5
        if "Fighting" in target_types:
            mult *= 0.5
        if "Ground" in target_types:
            mult *= 0.5
        if "Ice" in target_types:
            mult *= 2

    elif type == "Ghost":
        if "Ghost" in target_types:
            mult *= 2
        if "Psychic" in target_types:
            mult *= 2
        if "Normal" in target_types:
            mult *= 0
        if "Dark" in target_types:
            mult *= 0.5

    elif type == "Dragon":
        if "Dragon" in target_types:
            mult *= 2
        if "Steel" in target_types:
            mult *= 0.5
        if "Fairy" in target_types:
            mult *= 0

    elif type == "Dark":
        if "Ghost" in target_types:
            mult *= 2
        if "Dark" in target_types:
            mult *= 0.5
        if "Psychic" in target_types:
            mult *= 2
        if "Fairy" in target_types:
            mult *= 0.5
        if "Fighting" in target_types:
            mult *= 0.5

    elif type == "Steel":
        if "Steel" in target_types:
            mult *= 0.5
        if "Rock" in target_types:
            mult *= 2
        if "Ice" in target_types:
            mult *= 2
        if "Fairy" in target_types:
            mult *= 2
        if "Fire" in target_types:
            mult *= 0.5
        if "Water" in target_types:
            mult *= 0.5
        if "Electric" in target_types:
            mult *= 0.5

    elif type == "Fairy":
        if "Dragon" in target_types:
            mult *= 2
        if "Dark" in target_types:
            mult *= 2
        if "Fighting" in target_types:
            mult *= 2
        if "Poison" in target_types:
            mult *= 0.5
        if "Steel" in target_types:
            mult *= 0.5
        if "Fire" in target_types:
            mult *= 0.5

    return mult

def user_calc_damage(attacker: TrainedPokemon, target: TrainedPokemon, TM: TM, show_prints: bool) -> int:
    damage = TM[3]
    STAB = 1
    if TM[3] in [attacker[0][1], attacker[0][2]]:
        STAB = 1.5

    attack = 1
    defense = 1
    if TM[2] == "Physical":
        attack = attacker[1][1]
        defense = target[1][2]
    elif TM[2] == "Special":
        attack = attacker[1][3]
        defense = target[1][4]

    if TM[4] < 100:
        aux = random.randint(1, 100)
        if aux > TM[4]:
            if show_prints:
                time.sleep(1)
                print(f"{target[0][0]} avoided the attack.")
            return 0
        
    effectiveness = calc_effectiveness(TM[1], target)
    if 0 < effectiveness <= 0.5:
        if show_prints:
            time.sleep(1)
            print("It's not very effective.")
    elif effectiveness >= 2:
        if show_prints:
            time.sleep(1)
            print("It's super effective.")
    elif effectiveness == 0:
        if show_prints:
            time.sleep(1)
            print(f"It's doesn't affect {target[0][0]}.") 

    damage = ((18*damage*(attack/defense))/50 + 2)*STAB*effectiveness
    
    return int(damage)

def bot_calc_damage(attacker: TrainedPokemon, target: TrainedPokemon, TM: TM, show_prints: bool) -> int:
    damage = TM[3]
    STAB = 1
    if TM[3] in [attacker[0][1], attacker[0][2]]:
        STAB = 1.5

    attack = 1
    defense = 1
    if TM[2] == "Physical":
        attack = attacker[1][1]
        defense = target[1][2]
    elif TM[2] == "Special":
        attack = attacker[1][3]
        defense = target[1][4]

    if TM[4] < 100:
        aux = random.randint(1, 100)
        if aux > TM[4]:
            if show_prints:
                time.sleep(1)
                print(f"{target[0][0]} avoided the attack.")
            return 0
        
    effectiveness = calc_effectiveness(TM[1], target)
    if 0 < effectiveness <= 0.5:
        if show_prints:
            time.sleep(1)
            print("It's not very effective.")
    elif effectiveness >= 2:
        if show_prints:
            time.sleep(1)
            print("It's super effective.")
    elif effectiveness == 0:
        if show_prints:
            time.sleep(1)
            print(f"It's doesn't affect {target[0][0]}.") 

    damage = ((20*damage*(attack/defense))/50 + 2)*STAB*effectiveness
    
    return int(damage)

def share_weaknesses(pokemon1: TrainedPokemon, pokemon2: TrainedPokemon) -> bool:
    all_types = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting", "Poison", "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]
    weaknesses1 = []
    weaknesses2 = []
    for pk_type in all_types:
        if calc_effectiveness(pk_type, pokemon1) > 1:
            weaknesses1.append(pk_type)
        if calc_effectiveness(pk_type, pokemon2) > 1:
            weaknesses2.append(pk_type)

    for weakness in weaknesses1:
        if weakness in weaknesses2:
            return True
        
    return False