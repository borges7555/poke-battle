from typing import List

TM_Category = "Physical" | "Special" | "Status"
Type = "Normal" | "Fire" | "Water" | "Electric" | "Grass" | "Ice" | "Fighting" | "Poison" | "Ground" | "Flying" | "Psychic" | "Bug" | "Rock" | "Ghost" | "Dragon" | "Dark" | "Steel" | "Fairy"
TM = List[str, Type, TM_Category, int, int]
TrainedPokemon = List[List, TM, TM, TM, TM]
PokemonTeam = List[TrainedPokemon, TrainedPokemon, TrainedPokemon, TrainedPokemon, TrainedPokemon, TrainedPokemon]
Trainer = List[str, PokemonTeam]