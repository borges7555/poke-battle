from create_trainers import *
from returns import *

def create_default_trainers(pokemon_data: list, tm_data: list) -> list[Trainer]:
    trainers = []
    #Red
    Pikachu = return_pokemon_species("Pikachu", pokemon_data)
    MegaCharizardY = return_pokemon_species("Mega Charizard Y", pokemon_data)
    Blastoise = return_pokemon_species("Blastoise", pokemon_data)
    Venusaur = return_pokemon_species("Venusaur", pokemon_data)
    Snorlax = return_pokemon_species("Snorlax", pokemon_data)
    Mewtwo = return_pokemon_species("Mewtwo", pokemon_data)
    Red_Pikachu = create_TrainedPokemon(Pikachu, Pikachu[4:], return_TM("Thunderbolt", tm_data), return_TM("Surf", tm_data), return_TM("Play Rough", tm_data), return_TM("Brick Break", tm_data))
    Red_MegaCharizardY = create_TrainedPokemon(MegaCharizardY, MegaCharizardY[4:], return_TM("Flamethrower", tm_data), return_TM("Air Slash", tm_data), return_TM("Dragon Pulse", tm_data), return_TM("Scorching Sands", tm_data))
    Red_Blastoise = create_TrainedPokemon(Blastoise, Blastoise[4:], return_TM("Surf", tm_data), return_TM("Ice Beam", tm_data), return_TM("Flash Cannon", tm_data), return_TM("Dark Pulse", tm_data))
    Red_Venusaur = create_TrainedPokemon(Venusaur, Venusaur[4:], return_TM("Giga Drain", tm_data), return_TM("Sludge Bomb", tm_data), return_TM("Earthquake", tm_data), return_TM("Petal Blizzard", tm_data))
    Red_Snorlax = create_TrainedPokemon(Snorlax, Snorlax[4:], return_TM("Body Slam", tm_data), return_TM("Earthquake", tm_data), return_TM("Crunch", tm_data), return_TM("Body Press", tm_data))
    Red_Mewtwo = create_TrainedPokemon(Mewtwo, Mewtwo[4:], return_TM("Psychic", tm_data), return_TM("Shadow Ball", tm_data), return_TM("Aura Sphere", tm_data), return_TM("Ice Beam", tm_data))

    Red_Pikachu[1][1] *= 2
    Red_Pikachu[1][2] *= 2
    Red_Pikachu[1][3] *= 2
    Red_Pikachu[1][4] *= 2
    Red_Team = create_PokemonTeam(Red_Pikachu, Red_MegaCharizardY, Red_Blastoise, Red_Venusaur, Red_Snorlax, Red_Mewtwo)
    Red = create_Trainer("Red", Red_Team)
    trainers.append(Red)

    #Lance
    Aerodactyl = return_pokemon_species("Aerodactyl", pokemon_data)
    MegaGyarados = return_pokemon_species("Mega Gyarados", pokemon_data)
    Garchomp = return_pokemon_species("Garchomp", pokemon_data)
    Charizard = return_pokemon_species("Charizard", pokemon_data)
    Dragonite = return_pokemon_species("Dragonite", pokemon_data)
    Lugia = return_pokemon_species("Lugia", pokemon_data)
    Lance_Aerodactyl = create_TrainedPokemon(Aerodactyl, Aerodactyl[4:], return_TM("Rock Slide", tm_data), return_TM("Fly", tm_data), return_TM("Earthquake", tm_data), return_TM("Thunder Fang", tm_data))
    Lance_MegaGyarados = create_TrainedPokemon(MegaGyarados, MegaGyarados[4:], return_TM("Waterfall", tm_data), return_TM("Earthquake", tm_data), return_TM("Crunch", tm_data), return_TM("Ice Fang", tm_data))
    Lance_Garchomp = create_TrainedPokemon(Garchomp, Garchomp[4:], return_TM("Outrage", tm_data), return_TM("Earthquake", tm_data), return_TM("Poison Jab", tm_data), return_TM("Crunch", tm_data))
    Lance_Charizard = create_TrainedPokemon(Charizard, Charizard[4:], return_TM("Flamethrower", tm_data), return_TM("Air Slash", tm_data), return_TM("Dragon Pulse", tm_data), return_TM("Scorching Sands", tm_data))
    Lance_Dragonite = create_TrainedPokemon(Dragonite, Dragonite[4:], return_TM("Outrage", tm_data), return_TM("Fly", tm_data), return_TM("Thunder Punch", tm_data), return_TM("Brick Break", tm_data))
    Lance_Lugia = create_TrainedPokemon(Lugia, Lugia[4:], return_TM("Future Sight", tm_data), return_TM("Brave Bird", tm_data), return_TM("Thunderbolt", tm_data), return_TM("Ice Beam", tm_data))

    Lance_Team = create_PokemonTeam(Lance_Aerodactyl, Lance_MegaGyarados, Lance_Garchomp, Lance_Charizard, Lance_Dragonite, Lance_Lugia)
    Lance = create_Trainer("Lance", Lance_Team)
    trainers.append(Lance)

    #Steven
    Archeops = return_pokemon_species("Archeops", pokemon_data)
    Claydol = return_pokemon_species("Claydol", pokemon_data)
    Aggron = return_pokemon_species("Aggron", pokemon_data)
    Salamence = return_pokemon_species("Salamence", pokemon_data)
    MegaMetagross = return_pokemon_species("Mega Metagross", pokemon_data)
    PrimalKyogre = return_pokemon_species("Primal Kyogre", pokemon_data)
    Steven_Archeops = create_TrainedPokemon(Archeops, Archeops[4:], return_TM("Rock Slide", tm_data), return_TM("Fly", tm_data), return_TM("Earthquake", tm_data), return_TM("Crunch", tm_data))
    Steven_Claydol = create_TrainedPokemon(Claydol, Claydol[4:], return_TM("Psychic", tm_data), return_TM("Earth Power", tm_data), return_TM("Shadow Ball", tm_data), return_TM("Solar Beam", tm_data))
    Steven_Aggron = create_TrainedPokemon(Aggron, Aggron[4:], return_TM("Earthquake", tm_data), return_TM("Iron Head", tm_data), return_TM("Rock Slide", tm_data), return_TM("Body Press", tm_data))
    Steven_Salamence = create_TrainedPokemon(Salamence, Salamence[4:], return_TM("Outrage", tm_data), return_TM("Fly", tm_data), return_TM("Flamethrower", tm_data), return_TM("Shadow Claw", tm_data))
    Steven_MegaMetagross = create_TrainedPokemon(MegaMetagross, MegaMetagross[4:], return_TM("Iron Head", tm_data), return_TM("Thunder Punch", tm_data), return_TM("Psychic Fangs", tm_data), return_TM("Body Press", tm_data))
    Steven_PrimalKyogre = create_TrainedPokemon(PrimalKyogre, PrimalKyogre[4:], return_TM("Surf", tm_data), return_TM("Thunderbolt", tm_data), return_TM("Ice Beam", tm_data), return_TM("Brick Break", tm_data))

    Steven_Team = create_PokemonTeam(Steven_Archeops, Steven_Claydol, Steven_Aggron, Steven_Salamence, Steven_MegaMetagross, Steven_PrimalKyogre)
    Steven = create_Trainer("Steven", Steven_Team)
    trainers.append(Steven)

    #Cynthia

    #N

    #Diantha

    #Kukui

    #Leon

    #Geeta

    return trainers