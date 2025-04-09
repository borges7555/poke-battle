from create_trainers import *
from data_types import *
from returns import *
from prints import *

def user_create_trainer(pokemon_data: list, tm_data) -> Trainer:
    print("Choose your nickname:")
    nickname = input()
    trainer = []
    trainer.append(nickname)
    team = []
    used_pokemmons = []
    i = 0
    while i < 1: #TODO: change this to 6 to create a full team
        used_tms = []
        chosen_pokemon = []
        print(f"\nChoose pokemon number {i + 1}:")
        aux = input()
        #mostrar stats de pokemon se houver ' -s'
        if " -s" in aux:
            pokemon = return_pokemon_species(aux.split(" -")[0], pokemon_data)
            if pokemon is None:
                print("\nPokemon not found.")
            else:
                print_pokemon_stats(pokemon)

            continue
        elif " -l" in aux: #lista os pokemons que tem o excerto no nome
            print("")
            exists = False
            for pk in pokemon_data:
                if aux.split(" -")[0].lower() in pk[0].lower():
                    exists = True
                    print(pk[0])

            if not exists:
                print(f"Didn't find any pokemon with {aux.split(" -")[0].lower()} in its name.")

            continue

        pokemon = return_pokemon_species(aux, pokemon_data)
        if pokemon is None:
            print("\nPokemon not found.")
        elif pokemon in used_pokemmons:
            print("\nYou can't use the same pokemon more than once.")
        else:
            if not show_picture(aux.lower()):
                print(f"Couldn't show picture of {pokemon[0]}")

            used_pokemmons.append(pokemon)
            chosen_pokemon.append(pokemon)
            current_stats = pokemon[4:]
            chosen_pokemon.append(current_stats)
            k = 0
            while k < 4:
                print(f"Choose the TM number {k + 1} for {pokemon[0]}:")
                aux = input()
                #mostrar stats de tm se houver ' -s'
                if " -s" in aux:
                    tm = return_TM(aux.split(" -")[0], tm_data)
                    if tm is None:
                        print("\nTM not found.\n")
                    else:
                        print_tm_stats(tm)

                    continue
                elif " -l" in aux: #lista todos os ataques do tipo
                    exists = False
                    print("")
                    for move in tm_data:
                        if aux.split(" -")[0].lower() == move[1].lower():
                            exists = True
                            print(move[0])

                    if not exists:
                        print(f"{aux.split(" -")[0].lower()} type doesn't exist.\n")
                    else:
                        print("")

                    continue

                print("")

                tm = return_TM(aux, tm_data)
                if tm is None:
                    print("TM not found.")
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