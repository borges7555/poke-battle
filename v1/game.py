from prints import *
from create_defaul_trainers import *
from data_types import *
from battle_calcs import *
from show_pic import *

def game(trainer: Trainer, trainers: list):
    print("\nChoose a trainer to fight against:")
    for i in range(len(trainers)):
        print(f"{i + 1}. {trainers[i][0]}")

    aux = int(input())
    while aux < 1 or aux > len(trainers):
        print("\nInvalid input. Try again.")
        aux = int(input())

    opponent = trainers[aux - 1]
    while True:
        pk_in_batlle_user = 0
        pk_in_batlle_opponent = 0
        if not show_pictures([trainer[1][pk_in_batlle_user][0][0], opponent[1][pk_in_batlle_opponent][0][0]]):
            print("Couldn't show pictures of the pokemons")
        break

    return