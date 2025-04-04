from create_trainers import *
from data_types import *
from returns import *

def user_create_trainer(pokemon_data: list, tm_data) -> Trainer:
    print("Choose your nickname:")
    nickname = input()
    trainer = []
    trainer.append(nickname)
    team = []
    i = 0
    while i < 1: # Change this to 6 to create a full team
        chosen_pokemon = []
        print(f"\nChoose pokemon number {i + 1}:")
        aux = input()
        pokemon = return_pokemon_species(aux, pokemon_data)
        if pokemon is None:
            print("Please choose a valid pokemon.")
        else:
            chosen_pokemon.append(pokemon)
            current_hp = pokemon[4]
            chosen_pokemon.append(current_hp)
            k = 0
            while k < 4:
                print(f"\nChoose the TM number {k + 1} for {pokemon[0]}:")
                aux = input()
                tm = return_TM(aux, tm_data)
                if tm is None:
                    print("Please choose a valid TM.")
                else:
                    if not is_tm_and_pokemon_compatible(tm, pokemon[0]):
                        print("Please choose a compatible TM.")
                    else:
                        chosen_pokemon.append(tm)
                        k += 1

            team.append(chosen_pokemon)
            i += 1

    trainer.append(team)
    return trainer