def help():
    print("\nThe goal of the game is to win the pokemon battle.")
    print("You win the battle by knocking out all the opponent's pokemons.")
    print("The battle is a 1v1, and each trainer has 6 pokemons.")
    print("First, you have to create your team of 6 Pokemons.")
    print("Then, you choose the trainers you want to fight against.")
    print("The order of which pokemon moves first is based on its speed stat.") 
    print("In each turn, you have to choose an attack for your pokemon to use.")


def print_stats(name: str, data: list):
    info = next((row for row in data if row[0].lower() == name.lower()), None)
    if info != None:
        print("\n" + info[0] + ":")
        print("Type 1: " + info[1])
        print("Type 2: " + info[2])
        print("HP : " + str(info[4]))
        print("Att: " + str(info[5]))
        print("Def: " + str(info[6]))
        print("Spa: " + str(info[7]))
        print("Spd: " + str(info[8]))
        print("Spe: " + str(info[9]))
    else:
        print("\nPokemon not found, try again: ")