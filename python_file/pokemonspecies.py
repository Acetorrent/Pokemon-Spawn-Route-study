import random

class pokemonSpecies:

    possible_xp_groups = ('Fast', 'Medium Fast', 'Medium Slow', 'Slow', 'Erratic', 'Fluctuating')

    def __init__(
            
            self,
 
            iD: int = None,
            name: str = None, 
            type: list = None,

            height: float = None,
            weight: float = None,
            description: str = None,
            

            gender_ratio: dict = None,
            available_ability: dict = None,
            hatch_time: int = None,
            level_rate: str = None,
            base_friendship: int = None,

            base_stat: dict = None, 
            catch_rate: int = None,
            available_moves: list = None,
            xp_yield: dict = None,
            EV_yield: dict = None,

            *args,
            **kwargs

            ):


        #----------------CORE SPECIES STATS (IMMUTABLE)------------------#

        #Core Identification:
        self.iD = iD
        self.name = name
        self.type = type
        

        #Trivia Information
        self.height = height
        self.weight = weight
        self.description = description
        
        #Breeding Statistic:
        self.gender_ratio = gender_ratio
        self.available_ability = available_ability

        self.possible_nature = ('Lonely', 'Adamant', 'Bashful', 'Brave', 'Brave', 'Bold', 'Calm', 'Careful', 'Docile', 'Gentle', 'Hardy', 'Hasty', 'Impish', 'Jolly', 'Lax', 'Mild', 'Modest', 'Naive', 'Naughty', 'Quiet', 'Quirky', 'Rash', 'Relaxed', 'Sassy', 'Serious', 'Timid')

        self.hatch_time = hatch_time
        
        #Leveling Rate and XP Calculation
        self.leveling_rate = level_rate
        self.base_friendship = base_friendship

        #Moves Pool and Move list
        self.available_moves = available_moves

        #Base Stat
        self.base_stat = base_stat

        #Catch Rate
        self.catch_rate = catch_rate

        #Rewards From Defeat:
        self.xp_yield = xp_yield
        self.EV_yield = EV_yield

        #Post Calculation Dataset:

        self.neutral_nature = ('Hardy', 'Docile', 'Serious', 'Bashful', 'Quirky')
        self.nature_mod_list = {

      #attack Boost
      'Adamant': {'attack': 1.1, 'special-attack': 0.9}, 
      'Brave': {'attack': 1.1, 'speed': 0.9},
      'Lonely': {'attack': 1.1, 'defense': 0.9},
      'Naughty': {'attack': 1.1, 'special-defense': 0.9},

      #defense Boost
      'Bold': {'defense': 1.1, 'attack': 0.9}, 
      'Relaxed': {'defense': 1.1, 'speed': 0.9}, 
      'Impish': {'defense': 1.1, 'special-attack': 0.9}, 
      'Lax': {'defense': 1.1, 'special-defense': 0.9},

      #speed Boost
      'Timid': {'speed': 1.1, 'attack': 0.9},
      'Hasty': {'speed': 1.1, 'defense': 0.9}, 
      'Jolly': {'speed': 1.1, 'special-attack': 0.9},
      'Naive': {'speed': 1.1, 'special-defense': 0.9}, 

      #special attack Boost
      'Modest': {'special-attack': 1.1, 'attack': 0.9},
      'Mild': {'special-attack': 1.1, 'defense': 0.9},  
      'Quiet': {'special-attack': 1.1, 'speed': 0.9}, 
      'Rash': {'special-attack': 1.1, 'special-defense': 0.9}, 

      #special defense Boost
      'Calm': {'special-defense': 1.1, 'attack': 0.9}, 
      'Careful': {'special-defense': 1.1, 'special-attack': 0.9}, 
      'Gentle': {'special-defense': 1.1, 'defense': 0.9}, 
      'Sassy': {'special-defense': 1.1, 'speed': 0.9}
      }
        
        if self.base_stat is None:
            base_stat = {'hp': 0, 'attack': 0, 'special-attack': 0, 'defense': 0, 'special-defense': 0, 'speed': 0}


class newPokemon(pokemonSpecies):   


    #Init the class keeping the previous class stats as inheritance
    def __init__ (self, nick_name = None, level = 50, nature = None, *args, **kwargs):    

        #----------------INDIVIDUAL POKEMON STAT (MUTABLE)------------------#

        super().__init__(*args, **kwargs)

        #Identification:
        self.nick_name = nick_name


        self.level = level

        #EVs and IVs listing
        self.EV = {'hp': 0, 'attack': 0, 'special-attack': 0, 'defense': 0, 'special-defense': 0, 'speed': 0}
        self.IV = {'hp': 0, 'attack': 0, 'special-attack': 0, 'defense': 0, 'special-defense': 0, 'speed': 0}

        #Final Base stat Calculation
        self.final_stat = {}
        self.nature = None
        self.nature_mod = {'attack': 1, 'special-attack': 1, 'defense': 1, 'special-defense': 1, 'speed': 1}


        #Additional Built-In Functions Setup:

        #-Randomly initializes a Nature:
        self.set_random_nature()
        self.set_IV()
    

    def __repr__(self) -> str:
        return (f"\n--------------------------------------------\n{self.name} | Lvl. {self.level} | {self.nature} \n--IV: {self.IV}\n--Final Stat: {self.final_stat}\n--------------------------------------------\n")

    #----Minor Functions----#

    #Set or Randomize the Pokemon IVs upon Created
    def set_IV(self, health = random.randint(0, 31), attack = random.randint(0, 31), defense = random.randint(0, 31), sp_attack = random.randint(0, 31), sp_defense = random.randint(0, 31), speed = random.randint(0, 31)):
      
        self.IV.update({"health": health, "attack": attack, "special-attack": sp_attack, "defense": defense, "special-defense": sp_defense, "speed": speed})
        self.refresh_stat()


    #Function that set a random nature to the pokemon
    def set_random_nature(self):

        #Internal Import for the operation
        import random

        #Variable for simplicity
        a = self.possible_nature #List of Possible Nature

        self.nature = a[random.randint(0, len(a) - 1)]

        #Apply the new stat changes by nature
        self.refresh_nature_mod()
        self.refresh_stat()


    #Refresh the nature modifier after the change
    def refresh_nature_mod(self):
      
        a = self.possible_nature
        b = self.neutral_nature
        c = self.nature_mod_list

        #Checking if the nature is in the nature list
        if self.nature in a:

            #Check if the nature is in the neutral nature list
            if self.nature in b:
                return
            
            #Check against the modifier board list, which is 1.1 increase and which stat will be 0.9 decrease
            elif self.nature in c:
                self.nature_mod.update(c[self.nature])

        #No identifier of similar name found          
        else:
            print('\n\nInvalid Nature, {self.nature}, list of available nature:\n{self.possible_nature}')
        

    #Refresh each time Final stat formula Parameter (level, IV, EV, Base) is changed, or reset to the Default state
    def refresh_stat(self):

        #Reflect the new stat using EV, IV, health and other 
        self.final_stat.update({
          
            'hp': int((((2 * self.base_stat['hp'] + self.IV['hp'] + ((self.EV['hp'])/4)) * self.level)/100) + self.level + 10), 

            'attack': int((int(((2 * self.base_stat['attack'] + self.IV['attack'] + (self.EV['attack']/4)) * self.level) / 100) + 5) * self.nature_mod['attack']), 

            'special-attack': int((int(((2 * self.base_stat['special-attack'] + self.IV['special-attack'] + (self.EV['special-attack']/4)) * self.level) / 100) + 5) * self.nature_mod['special-attack']), 

            'defense': int((int(((2 * self.base_stat['defense'] + self.IV['defense'] + (self.EV['defense']/4)) * self.level) / 100) + 5) * self.nature_mod['defense']), 

            'special-defense': int((int(((2 * self.base_stat['special-defense'] + self.IV['special-defense'] + (self.EV['special-defense']/4)) * self.level) / 100) + 5) * self.nature_mod['special-defense']), 

            'speed': int((int(((2 * self.base_stat['speed'] + self.IV['speed'] + (self.EV['speed']/4)) * self.level) / 100) + 5) * self.nature_mod['speed'])
          
        })






        



