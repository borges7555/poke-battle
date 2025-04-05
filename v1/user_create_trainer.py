from create_trainers import *
from data_types import *
from returns import *

def user_create_trainer(pokemon_data: list, tm_data) -> Trainer:
    print("Choose your nickname:")
    nickname = input()
    trainer = []
    trainer.append(nickname)
    team = []
    used_pokemmons = []
    i = 0
    while i < 1: # Change this to 6 to create a full team
        used_tms = []
        chosen_pokemon = []
        print(f"\nChoose pokemon number {i + 1}:")
        aux = input()
        pokemon = return_pokemon_species(aux, pokemon_data)
        if pokemon is None:
            print("\nPlease choose a valid pokemon.")
        elif pokemon in used_pokemmons:
            print("\nYou can't use the same pokemon more than once.")
        else:
            used_pokemmons.append(pokemon)
            chosen_pokemon.append(pokemon)
            current_stats = pokemon[4:]
            chosen_pokemon.append(current_stats)
            k = 0
            while k < 4:
                print(f"\nChoose the TM number {k + 1} for {pokemon[0]}:")
                aux = input()
                tm = return_TM(aux, tm_data)
                if tm is None:
                    print("Please choose a valid TM.")
                elif tm in used_tms:
                    print("\nYou can't use the same TM more than once in the same pokemon.")
                else:
                    if not is_tm_and_pokemon_compatible(tm, pokemon[0]):
                        print("\nPlease choose a compatible TM.")
                    else:
                        used_tms.append(tm)
                        chosen_pokemon.append(tm)
                        k += 1

            team.append(chosen_pokemon)
            i += 1

    trainer.append(team)
    return trainer