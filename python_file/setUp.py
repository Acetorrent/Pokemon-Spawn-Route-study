import pokemonspecies as pkmn
import requests
from collections import defaultdict
import random

base = 'https://pokeapi.co/api/v2/'

current_pokemon_list = []

def change_zone(number: str):

    number = str(number)

    data = {}

    d = requests.get(base + f'location-area/{number}/')

    for pokemon in d.json()['pokemon_encounters']:
        current_pokemon_list.append(pokemon['pokemon']['name'])



def create(pokemon):

    data = {}

    if pokemon is not None:
        d = requests.get(base + f"pokemon/{pokemon}/")
        for move in d.json()['stats']:
            data.update({str(move['stat']['name']) : move['base_stat']})

    enemy = pkmn.newPokemon(name = (d.json()['name']).title(), base_stat = data)
    
    print (enemy.name)
    print (enemy.nature)
    print (enemy.nature_mod)
    print (enemy.final_stat)
