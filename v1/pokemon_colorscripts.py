import json
import os
from create_map import get_file_path

PROGRAM = os.path.realpath(__file__)
PROGRAM_DIR = os.path.dirname(PROGRAM)
COLORSCRIPTS_DIR = get_file_path("colorscripts")
REGULAR_SUBDIR = "regular"
SMALL_SUBDIR = "small"

def print_file(filepaths: list) -> None:
    with open(filepaths[0], "r") as f, open(filepaths[1], "r") as s:
        print(f.read() + s.read())

def show_pokemon_by_name(name1: str, name2: str, form1: str = "", form2: str = "") -> bool:
    base_path = COLORSCRIPTS_DIR
    color_subdir =  REGULAR_SUBDIR
    size_subdir =  SMALL_SUBDIR
    json_path = get_file_path("pokemon.json")
    pokemon_files = []
    for i in range (2):
        if i == 0:
            name = name1.lower()
            form = form1.lower()
        else:
            name = name2.lower()
            form = form2.lower()
        print(f"Showing picture of {name} {form}.")

        with open(f"{json_path}") as file:
            pokemon_json = json.load(file)
            pokemon_names = {pokemon["name"] for pokemon in pokemon_json}
            if name not in pokemon_names:
                print(f"\nCouldn't show picture of {name}\n")
                return False

            if form:
                for pokemon in pokemon_json:
                    if pokemon["name"] == name:
                        forms = pokemon["forms"]
                        alternate_forms = [f for f in forms if f != "regular"]
                if form in alternate_forms:
                    name += f"-{form}"
                else:
                    print(f"Invalid form '{form}' for pokemon {name}")
                    if not alternate_forms:
                        print(f"No alternate forms available for {name}")
                    else:
                        print(f"Available alternate forms are")
                        for form in alternate_forms:
                            print(f"- {form}")
                    return False
            
        pokemon_file = f"{base_path}/{size_subdir}/{color_subdir}/{name}"
        pokemon_files.append(pokemon_file)

    print("")
    print_file(pokemon_files)
    return True

def check_if_exists(name: str, form: str = "") -> bool:
    base_path = COLORSCRIPTS_DIR
    color_subdir =  REGULAR_SUBDIR
    size_subdir =  SMALL_SUBDIR
    json_path = get_file_path("pokemon.json")
    with open(f"{json_path}") as file:
        pokemon_json = json.load(file)
        pokemon_names = {pokemon["name"] for pokemon in pokemon_json}
        if name not in pokemon_names:
            #print(f"Couldn't show picture of {name}\n")
            return False

        if form:
            for pokemon in pokemon_json:
                if pokemon["name"] == name:
                    forms = pokemon["forms"]
                    alternate_forms = [f for f in forms if f != "regular"]
            if form in alternate_forms:
                name += f"-{form}"
            else:
                print(f"Invalid form '{form}' for pokemon {name}")
                if not alternate_forms:
                    print(f"No alternate forms available for {name}")
                else:
                    print(f"Available alternate forms are")
                    for form in alternate_forms:
                        print(f"- {form}")
                return False
            
    pokemon_file = f"{base_path}/{size_subdir}/{color_subdir}/{name}"
    #print("")
    #print_file(pokemon_file)
    return True