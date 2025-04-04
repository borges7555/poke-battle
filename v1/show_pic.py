from pokemon_colorscripts import *

def show_pictures(names: list) -> bool:
    aux = []
    for i in range(2):
        if "alolan" in names[i]:
            aux.append([names[i].split(" ")[1], "alola"])
        elif "galarian" in names:
            aux.append(names[i].split(" ")[1], "galar")
        elif "hisuian" in names:
            aux.append(names[i].split(" ")[1], "hisui")
        elif "paldean" in names[i]:
            aux.append(names[i].split(" ")[1], "paldea")
        elif "mega" in names[i]:
            if len(names[i].split(" ")) == 2:
                aux.append(names[i].split(" ")[1], "mega")
            elif 'x' in names[i]:
                aux.append(names[i].split(" ")[1], "mega-x")
            elif 'y' in names[i]:
                aux.append(names[i].split(" ")[1], "mega-y")
        elif "primal" in names[i]:
            aux.append(names[i].split(" ")[1], "primal")
        elif "incarnate" in names[i]:
            aux.append(names[i].split(" ")[0])
        elif len(names[i].split(" ")) == 2:
            if not check_if_exists(names[i].split(" ")[0], names[i].split(" ")[1]):
                if not check_if_exists(names[i].split(" ")[1], names[i].split(" ")[0]):
                    if not check_if_exists(names[i].split(" ")[0] + "-" + names[i].split(" ")[1]):
                        i = i
                    else:
                        aux.append(names[i].split(" ")[0] + "-" + names[i].split(" ")[1])
                else:
                    aux.append(names[i].split(" ")[1], names[i].split(" ")[0])
            else:
                aux.append(names[i].split(" ")[0], names[i].split(" ")[1])
        else:
            aux.append([names[i], ""])
        
    return show_pokemon_by_name(aux[0][0], aux[1][0], aux[0][1], aux[1][1])