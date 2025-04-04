from game import game
from prints import help
from create_map import *
from user_create_trainer import *
from create_defaul_trainers import *
import sys

def main() -> int:
    print("Welcome to the Pokemon Battle!")
    print("Type 'help' for instructions, 'exit' to leave or press 'Enter' to start the game.")
    aux = input()

    while aux != 'help' and aux != 'exit' and aux != '':
        print("\nInvalid input. Try again.")
        aux = input()
        
    if aux == 'help':
        help()
        print("If you want to see this again, type 'help'.")
        print("Press 'Enter' to start the game.")
        input()
    elif aux == 'exit':
        sys.exit(1)

    play_again = True
    pokemon_data = create_pokemon_map_from_csv()
    tm_data = create_tm_map_from_csv()
    trainers = create_default_trainers(pokemon_data, tm_data)
    while play_again:
        trainer = user_create_trainer(pokemon_data, tm_data)
        game(trainer, trainers)
        print("Do you want to play again? (y/n)")
        aux = input()
        while aux != 'y' and aux != 'n':
            print("\nInvalid input. Try again.")
            aux = input()

        if aux == 'n':
            play_again = False

        print()
        
    return 0


if __name__ == "__main__":
    main()