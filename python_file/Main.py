import pokemonspecies as pkmn
import requests
from collections import defaultdict
import random
import os

base = 'https://pokeapi.co/api/v2/'

current_pokemon_list = []

player_pokemon = None
route_res = False
enemy_pokemon = None


def change_zone(number: str):

    number = str(number)

    r = requests.get(base + f'location-area/')

    #Select the index value json
    request_data = (r.json()['results'])[int(number)]
    url = request_data['url']

    print (url)
    print (request_data['name'])

    d = requests.get(url)

    data = d.json()

    if d is None:
        return
    #Checking json
    if d.ok:

        for pokemon in d.json()['pokemon_encounters']:
            current_pokemon_list.append(pokemon['pokemon']['name'])
        

        name = data['location']['name']

        name = name.replace("-", " ")
        name = name.title()

        print (f"---------\nRoute Changed to '{name}':\n---------")

        print(f"possible encounter: {current_pokemon_list}\n\n")

        return True

    else:
        return False

def random_from_route(pkmn: list):
    import random

    name = pkmn[random.randint(0, (len(pkmn) - 1))]

    return name


def create(pokemon: str):

    data = {}

    if pokemon is not None:
        d = requests.get(base + f"pokemon/{pokemon}/")
        for move in d.json()['stats']:
            data.update({str(move['stat']['name']) : move['base_stat']})

    enemy = pkmn.newPokemon(name = (d.json()['name']).title(), base_stat = data)

    return enemy
    
    print (enemy.name)
    print (enemy.nature)
    print (enemy.nature_mod)
    print (enemy.final_stat)

def pokemon_exist(pokemon: str):
    if pokemon is not None:
        d = requests.get(base + f"pokemon/{pokemon}/")

        if d.ok:
            return True
        else:
            return False

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def battle_scene():

    print(f"""
                                            Enemy {enemy_pokemon.name}

                                                {enemy_pokemon}                    


----------------------------- VS ----------------------------------


Your {player_pokemon.name}:

    {player_pokemon}

          
          """)

def route_select():

    
    print("----------------\nSelect a location:\n \n-Enter any number to select\n-type 'random' to get a random route\n----------------")

    route_response = input("\n\nEnter choice: ")
    route_response.strip(" ")

    print(f"\nroute: {route_response}\n")



    if route_response.lower() == "random":
        num = random.randint(0, 732)
        change_zone(num)
        return True
    elif route_response.isnumeric():
        route_response = int(route_response)
        status = change_zone(route_response)

        if status:
            print ("--------------------\nConnect successful!\n--------------------")
            return True
        else:
            clear()
            print ("\nInvalid Entry Range\n")
            return False


    else:
        clear()
        print("\nInvalid Entry\n")
        return False       
    



while True:

    #Spawn Random Pokemon Encounter Each time:
    while player_pokemon is None:

        print("\n----Welcome to the Module! First, select a pokemon to get started!")



        player_pokemon_name = str(input(f"\nSelect Your Pokemon by typing the name of that pokemon: "))

        name_temp = player_pokemon_name

        player_pokemon_name.strip(" ")

        player_pokemon_name = player_pokemon_name.lower()
        player_pokemon_name.replace(" ", "-")

        if pokemon_exist(player_pokemon_name):
            print(f"\nPokemon Found! Initialize your starter with the name'{player_pokemon_name}'\n")
            player_pokemon = create(player_pokemon_name)
        else:
            print(f"\nNo such pokemon with name {player_pokemon_name} or {name_temp} found, please try again.\n")

    
    input("\n--------Initialize Complete, Press Enter to Continue!--------\n")

    clear()

    #Select a Route:
    if not route_res:
        route_res = route_select()

    input("\n--------Press Enter to Continue!--------\n")

    clear()

    if route_res:
        action = input("""

    Select An Action:
            
        - Encounter
        - Switch Route    
        - Quit       

        Enter Your Option: """)


        action.strip(" ")
        action = action.lower()

        print(f"action: '{action}'\n")

        if action == "encounter":

            enemy_pokemon = create(random_from_route(current_pokemon_list))

            print ("\n Pokemon Encounter !\n")

            clear()

            print (f"\nA Wild {enemy_pokemon.name} has appeared! \n")
            
            input("\n Press Enter to Proceed ")

            clear()

            battle_scene()

            print("\n To be Added combat in the future\n")

            input("\n--------Press Enter to Continue!--------\n")

            clear()
        elif action == "switch route":
            route_res = False
            print (f"\nRoute Reset\n")
        
        elif action == "quit":
            input("\n--------Press Enter to Continue!--------\n")
            break
            
        else:
            print ("\nInvalid Entry\n")
            
input("\n--------Press Enter to Quit and Close--------\n")

    




