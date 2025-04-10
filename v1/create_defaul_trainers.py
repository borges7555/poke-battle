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
    Red_Pikachu[1][2] *= 1.5
    Red_Pikachu[1][3] *= 2
    Red_Pikachu[1][4] *= 1.5
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
    Spiritomb = return_pokemon_species("Spiritomb", pokemon_data)
    Magmortar = return_pokemon_species("Magmortar", pokemon_data)
    Milotic = return_pokemon_species("Milotic", pokemon_data)
    Lucario = return_pokemon_species("Lucario", pokemon_data)
    MegaGarchomp = return_pokemon_species("Mega Garchomp", pokemon_data)
    GiratinaOrigin = return_pokemon_species("Giratina Origin", pokemon_data)
    Cynthia_Spiritomb = create_TrainedPokemon(Spiritomb, Spiritomb[4:], return_TM("Poltergeist", tm_data), return_TM("Foul Play", tm_data), return_TM("Psychic", tm_data), return_TM("Burning Jealousy", tm_data))
    Cynthia_Magmortar = create_TrainedPokemon(Magmortar, Magmortar[4:], return_TM("Flamethrower", tm_data), return_TM("Thunderbolt", tm_data), return_TM("Scorching Sands", tm_data), return_TM("Solar Beam", tm_data))
    Cynthia_Milotic = create_TrainedPokemon(Milotic, Milotic[4:], return_TM("Surf", tm_data), return_TM("Ice Beam", tm_data), return_TM("Alluring Voice", tm_data), return_TM("Dragon Pulse", tm_data))
    Cynthia_Lucario = create_TrainedPokemon(Lucario, Lucario[4:], return_TM("Close Combat", tm_data), return_TM("Flash Cannon", tm_data), return_TM("Thunder Punch", tm_data), return_TM("Ice Punch", tm_data))
    Cynthia_MegaGarchomp = create_TrainedPokemon(MegaGarchomp, MegaGarchomp[4:], return_TM("Outrage", tm_data), return_TM("Earthquake", tm_data), return_TM("Poison Jab", tm_data), return_TM("Crunch", tm_data))
    Cynthia_GiratinaOrigin = create_TrainedPokemon(GiratinaOrigin, GiratinaOrigin[4:], return_TM("Poltergeist", tm_data), return_TM("Draco Meteor", tm_data), return_TM("Thunderbolt", tm_data), return_TM("Energy Ball", tm_data))

    Cynthia_Team = create_PokemonTeam(Cynthia_Spiritomb, Cynthia_Magmortar, Cynthia_Milotic, Cynthia_Lucario, Cynthia_MegaGarchomp, Cynthia_GiratinaOrigin)
    Cynthia = create_Trainer("Cynthia", Cynthia_Team)
    trainers.append(Cynthia)
    #N
    Darmanitan = return_pokemon_species("Darmanitan", pokemon_data)
    #Archeops
    Carracosta = return_pokemon_species("Carracosta", pokemon_data)
    KlinKlang = return_pokemon_species("Klinklang", pokemon_data)
    Zoroark = return_pokemon_species("Zoroark", pokemon_data)
    KyuremWhite = return_pokemon_species("Kyurem White", pokemon_data)
    N_Darmanitan = create_TrainedPokemon(Darmanitan, Darmanitan[4:], return_TM("Flare Blitz", tm_data), return_TM("Earthquake", tm_data), return_TM("Rock Slide", tm_data), return_TM("Thunder Punch", tm_data))
    N_Archeops = create_TrainedPokemon(Archeops, Archeops[4:], return_TM("Rock Slide", tm_data), return_TM("Fly", tm_data), return_TM("Earthquake", tm_data), return_TM("Crunch", tm_data))
    N_Carracosta = create_TrainedPokemon(Carracosta, Carracosta[4:], return_TM("Waterfall", tm_data), return_TM("Rock Slide", tm_data), return_TM("Iron Head", tm_data), return_TM("Earthquake", tm_data))
    N_KlinKlang = create_TrainedPokemon(KlinKlang, KlinKlang[4:], return_TM("Flash Cannon", tm_data), return_TM("Wild Charge", tm_data), return_TM("Facade", tm_data), return_TM("Power Gem", tm_data))
    N_Zoroark = create_TrainedPokemon(Zoroark, Zoroark[4:], return_TM("Dark Pulse", tm_data), return_TM("Flamethrower", tm_data), return_TM("Psychic", tm_data), return_TM("Focus Blast", tm_data))
    N_KyuremWhite = create_TrainedPokemon(KyuremWhite, KyuremWhite[4:], return_TM("Ice Beam", tm_data), return_TM("Draco Meteor", tm_data), return_TM("Flash Cannon", tm_data), return_TM("Earth Power", tm_data))
    N_Team = create_PokemonTeam(N_Darmanitan, N_Archeops, N_Carracosta, N_KlinKlang, N_Zoroark, N_KyuremWhite)
    N = create_Trainer("N", N_Team)
    trainers.append(N)
    #Diantha

    #Kukui

    #Leon

    #Geeta

    #Borges

    #Isaac
    Jolteon = return_pokemon_species("Jolteon", pokemon_data)
    Mamoswine = return_pokemon_species("Mamoswine", pokemon_data)
    AshGreninja = return_pokemon_species("Ash Greninja", pokemon_data)
    #Lucario
    MegaCharizardX = return_pokemon_species("Mega Charizard X", pokemon_data)
    Yveltal = return_pokemon_species("Yveltal", pokemon_data)
    Isaac_Jolteon = create_TrainedPokemon(Jolteon, Jolteon[4:], return_TM("Thunderbolt", tm_data), return_TM("Alluring Voice", tm_data), return_TM("Shadow Ball", tm_data), return_TM("Hyper Voice", tm_data))
    Isaac_Mamoswine = create_TrainedPokemon(Mamoswine, Mamoswine[4:], return_TM("Body Press", tm_data), return_TM("Earthquake", tm_data), return_TM("Icicle Spear", tm_data), return_TM("Rock Slide", tm_data))
    Isaac_AshGreninja = create_TrainedPokemon(AshGreninja, AshGreninja[4:], return_TM("Surf", tm_data), return_TM("Ice Beam", tm_data), return_TM("Dark Pulse", tm_data), return_TM("Sludge Wave", tm_data))
    Isaac_Lucario = create_TrainedPokemon(Lucario, Lucario[4:], return_TM("Close Combat", tm_data), return_TM("Flash Cannon", tm_data), return_TM("Thunder Punch", tm_data), return_TM("Ice Punch", tm_data))
    Isaac_MegaCharizardX = create_TrainedPokemon(MegaCharizardX, MegaCharizardX[4:], return_TM("Flare Blitz", tm_data), return_TM("Outrage", tm_data), return_TM("Earthquake", tm_data), return_TM("Solar Beam", tm_data))
    Isaac_Yveltal = create_TrainedPokemon(Yveltal, Yveltal[4:], return_TM("Foul Play", tm_data), return_TM("Fly", tm_data), return_TM("Psychic", tm_data), return_TM("Heat Wave", tm_data))

    Isaac_Team = create_PokemonTeam(Isaac_Jolteon, Isaac_Mamoswine, Isaac_AshGreninja, Isaac_Lucario, Isaac_MegaCharizardX, Isaac_Yveltal)
    Isaac = create_Trainer("Isaac", Isaac_Team)
    trainers.append(Isaac)
    return trainers