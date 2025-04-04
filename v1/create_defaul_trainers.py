from create_trainers import *
from returns import *

def create_default_trainers(data: list) -> list[Trainer]:
    trainers = []
    Red_Pikachu = create_TrainedPokemon[return_pokemon_species("Pikachu", data), return_TM("Thunderbolt"), return_TM("Surf"), return_TM("Play Rough"), return_TM("Brick Break")]
    Red_Charizard = create_TrainedPokemon[return_pokemon_species("Charizard", data), return_TM("Flamethrower"), return_TM("Air Slash"), return_TM("Dragon Pulse"), return_TM("Thunder Punch")]
    Red_Blastoise = create_TrainedPokemon[return_pokemon_species("Blastoise", data), return_TM("Surf"), return_TM("Ice Beam"), return_TM("Flash Cannon"), return_TM("Dark Pulse")]
    Red_Venusaur = create_TrainedPokemon[return_pokemon_species("Venusaur", data), return_TM("Giga Drain"), return_TM("Sludge Bomb"), return_TM("Earthquake"), return_TM("Petal Blizzard")]
    Red_Snorlax = create_TrainedPokemon[return_pokemon_species("Snorlax", data), return_TM("Body Slam"), return_TM("Earthquake"), return_TM("Ice Punch"), return_TM("Body Press")]
    Red_Mewtwo = create_TrainedPokemon[return_pokemon_species("Mewtwo", data), return_TM("Psychic"), return_TM("Shadow Ball"), return_TM("Aura Sphere"), return_TM("Ice Beam")]

    Red_Team = create_PokemonTeam[Red_Pikachu, Red_Charizard, Red_Blastoise, Red_Venusaur, Red_Snorlax, Red_Mewtwo]
    Red = create_Trainer("Red", Red_Team)
    trainers.append(Red)

    return trainers