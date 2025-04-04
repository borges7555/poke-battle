from data_types import *

def return_TM(name: str, data: list) -> TM:
    for tm in data:
        if tm[0].lower() == name.lower():
            return tm
    
    print(f"\nTM {name} not found.")
    return None

def return_pokemon_species(name: str, data: list) -> list:
    for pokemon in data:
        if pokemon[0].lower() == name.lower():
            return pokemon
        
    print(f"\nPokemon {name} not found.")
    return None

def is_tm_and_pokemon_compatible(tm: TM, pokemon: str) -> bool:
    is_compatible = True

    return is_compatible