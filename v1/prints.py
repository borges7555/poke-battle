from data_types import *
from show_pic import *

def help():
    print("\nThe goal of the game is to win the pokemon battle.")
    print("You win the battle by knocking out all the opponent's pokemons.")
    print("The battle is a 1v1, and each trainer has 6 pokemons.")
    print("First, you have to create your team of 6 Pokemons.")
    print("While creating your team, you can type <pokemon_name> or <tm_name> plus '-s' to be shown its stats.")
    print("Then, you choose the trainers you want to fight against.")
    print("The order of which pokemon moves first is based on its speed stat.") 
    print("In each turn, you have to choose an attack for your pokemon to use.")


def print_pokemon_stats(pokemon_data: list):
    print(f"\n{pokemon_data[0]}:")
    print(f"Type 1: {pokemon_data[1]}")
    print(f"Type 2: {pokemon_data[2]}")
    print(f"HP : {str(pokemon_data[4])}")
    print(f"Att: {str(pokemon_data[5])}")
    print(f"Def: {str(pokemon_data[6])}")
    print(f"Spa: {str(pokemon_data[7])}")
    print(f"Spd: {str(pokemon_data[8])}")
    print(f"Spe: {str(pokemon_data[9])}")


def print_tm_stats(tm_data: list):
    print(f"\n{tm_data[0]}:")
    print(f"Type: {tm_data[1]}")
    print(f"Category: {tm_data[2]}")
    print(f"Power: {str(tm_data[3])}")
    print(f"Accuracy: {str(tm_data[4])}")


def print_pokemons_in_battle(trainer: Trainer, pk_in_batlle_user: int, user_hp: int, opponent: Trainer, pk_in_batlle_opponent: int, opponent_hp: int):
    if show_picture(opponent[1][pk_in_batlle_opponent][0][0].lower()):
        print(f"HP: {opponent_hp}/{opponent[1][pk_in_batlle_opponent][0][4]}")
    else:
        print(f"Couldn't show picture of {opponent[1][pk_in_batlle_opponent][0][0]}")

    if show_picture(trainer[1][pk_in_batlle_user][0][0].lower()):
        print(f"HP: {user_hp}/{trainer[1][pk_in_batlle_user][0][4]}")
    else:
        print(f"Couldn't show picture of {trainer[1][pk_in_batlle_user][0][0]}")