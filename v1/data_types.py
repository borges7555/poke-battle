from typing import List, Tuple

TM_Category = "Physical" or "Special" or "Status"
Type = "Normal" or "Fire" or "Water" or "Electric" or "Grass" or "Ice" or "Fighting" or "Poison" or "Ground" or "Flying" or "Psychic" or "Bug" or "Rock" or "Ghost" or "Dragon" or "Dark" or "Steel" or "Fairy"
TM = Tuple[str, Type, TM_Category, int, int]
TrainedPokemon = Tuple[List, TM, TM, TM, TM]
PokemonTeam = Tuple[TrainedPokemon, TrainedPokemon, TrainedPokemon, TrainedPokemon, TrainedPokemon, TrainedPokemon]
Trainer = Tuple[str, PokemonTeam]