import random
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

    if type == "Fire":
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

    if type == "Water":
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

    if type == "Electric":
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

    if type == "Grass":
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

    if type == "Ice":
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

    if type == "Fighting":
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

    if type == "Poison":
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

    if type == "Ground":
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

    if type == "Flying":
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

    if type == "Psychic":
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

    if type == "Bug":
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

    if type == "Rock":
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

    if type == "Ghost":
        if "Ghost" in target_types:
            mult *= 2
        if "Psychic" in target_types:
            mult *= 2
        if "Normal" in target_types:
            mult *= 0
        if "Dark" in target_types:
            mult *= 0.5

    if type == "Dragon":
        if "Dragon" in target_types:
            mult *= 2
        if "Steel" in target_types:
            mult *= 0.5
        if "Fairy" in target_types:
            mult *= 0

    if type == "Dark":
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

    if type == "Steel":
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

    if type == "Fairy":
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

def calc_damage(attacker: TrainedPokemon, target: TrainedPokemon, TM: TM) -> int:
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
            print(f"\n{target[0][0]} avoided the attack.")
            return 0
        
    effectiveness = calc_effectiveness(TM[1], target)
    if 0 < effectiveness <= 0.5:
        print("\nIt's not very effective.")
    elif effectiveness >= 2:
        print("\nIt's super effective.")
    elif effectiveness == 0:
        print(f"\nIt's doesn't affect {target[0][0]}.") 

    damage = ((21*damage*(attack/defense))/50 + 2)*STAB*effectiveness
    
    return int(damage)