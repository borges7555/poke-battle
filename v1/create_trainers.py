from data_types import *

def create_Trainer(name: str, team: PokemonTeam) -> Trainer:
    return [name, team]

def create_TrainedPokemon(pokemon: list, current_hp: int, move1: str, move2: str, move3: str, move4: str) -> TrainedPokemon:
    return [pokemon, current_hp, move1, move2, move3, move4]

def create_PokemonTeam(pokemon1: TrainedPokemon, pokemon2: TrainedPokemon, pokemon3: TrainedPokemon, pokemon4: TrainedPokemon, pokemon5: TrainedPokemon, pokemon6: TrainedPokemon, ) -> PokemonTeam:
    return [pokemon1, pokemon2, pokemon3, pokemon4, pokemon5, pokemon6]