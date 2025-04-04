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

def calc_damage(attacker: TrainedPokemon, target: TrainedPokemon, TM: TM) -> float:
    damage = TM[3]
    STAB = 1
    if TM[3] in [attacker[0][1], attacker[0][2]]:
        STAB = 1.5

    attack, defense = 0
    if TM[2] == "Physical":
        attack = attacker[0][5]
        defense = target[0][7]
    elif TM[2] == "Special":
        attack = attacker[0][6]
        defense = target[0][8]

    effectiveness = calc_effectiveness(TM[1], target)

    damage = ((21*damage*(attack/defense))/50 + 2)*STAB*effectiveness
    
    return damage