from create_trainers import *
from returns import *

def create_default_trainers(pokemon_data: list, tm_data: list) -> list[Trainer]:
    trainers = []
    Red_Pikachu = create_TrainedPokemon(return_pokemon_species("Pikachu", pokemon_data), return_TM("Thunderbolt", tm_data), return_TM("Surf", tm_data), return_TM("Play Rough", tm_data), return_TM("Brick Break", tm_data))
    Red_Charizard = create_TrainedPokemon(return_pokemon_species("Charizard", pokemon_data), return_TM("Flamethrower", tm_data), return_TM("Air Slash", tm_data), return_TM("Dragon Pulse", tm_data), return_TM("Thunder Punch", tm_data))
    Red_Blastoise = create_TrainedPokemon(return_pokemon_species("Blastoise", pokemon_data), return_TM("Surf", tm_data), return_TM("Ice Beam", tm_data), return_TM("Flash Cannon", tm_data), return_TM("Dark Pulse", tm_data))
    Red_Venusaur = create_TrainedPokemon(return_pokemon_species("Venusaur", pokemon_data), return_TM("Giga Drain", tm_data), return_TM("Sludge Bomb", tm_data), return_TM("Earthquake", tm_data), return_TM("Petal Blizzard", tm_data))
    Red_Snorlax = create_TrainedPokemon(return_pokemon_species("Snorlax", pokemon_data), return_TM("Body Slam", tm_data), return_TM("Earthquake", tm_data), return_TM("Ice Punch", tm_data), return_TM("Body Press", tm_data))
    Red_Mewtwo = create_TrainedPokemon(return_pokemon_species("Mewtwo", pokemon_data), return_TM("Psychic", tm_data), return_TM("Shadow Ball", tm_data), return_TM("Aura Sphere", tm_data), return_TM("Ice Beam", tm_data))

    Red_Team = create_PokemonTeam(Red_Pikachu, Red_Charizard, Red_Blastoise, Red_Venusaur, Red_Snorlax, Red_Mewtwo)
    Red = create_Trainer("Red", Red_Team)
    trainers.append(Red)

    return trainers