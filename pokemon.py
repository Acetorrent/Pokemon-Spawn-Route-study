class pokemon:

    import random
  
    #List of All Nature
    possible_nature = ("Lonely", "Adamant", "Bashful", "Brave", "Brave", "Bold", "Calm", "Careful", "Docile", "Gentle", "Hardy", "Hasty", "Impish", "Jolly", "Lax", "Mild", "Modest", "Naive", "Naughty", "Quiet", "Quirky", "Rash", "Relaxed", "Sassy", "Serious", "Timid")

    #List of Neutral Nature 
    neutral_nature = ("Hardy", "Docile", "Serious", "Bashful", "Quirky")

    #List of Modifying Nature
    nature_mod_list = {

      #Attack Boost
      "Adamant": {"Attack": 1.1, "Special Attack": 0.9}, 
      "Brave": {"Attack": 1.1, "Speed": 0.9},
      "Lonely": {"Attack": 1.1, "Defense": 0.9},
      "Naughty": {"Attack": 1.1, "Special Defense": 0.9},

      #Defense Boost
      "Bold": {"Defense": 1.1, "Attack": 0.9}, 
      "Relaxed": {"Defense": 1.1, "Speed": 0.9}, 
      "Impish": {"Defense": 1.1, "Special Attack": 0.9}, 
      "Lax": {"Defense": 1.1, "Special Defense": 0.9},

      #Speed Boost
      "Timid": {"Speed": 1.1, "Attack": 0.9},
      "Hasty": {"Speed": 1.1, "Defense": 0.9}, 
      "Jolly": {"Speed": 1.1, "Special Attack": 0.9},
      "Naive": {"Speed": 1.1, "Special Defense": 0.9}, 

      #Special Attack Boost
      "Modest": {"Special Attack": 1.1, "Attack": 0.9},
      "Mild": {"Special Attack": 1.1, "Defense": 0.9},  
      "Quiet": {"Special Attack": 1.1, "Speed": 0.9}, 
      "Rash": {"Special Attack": 1.1, "Special Defense": 0.9}, 

      #Special Defense Boost
      "Calm": {"Special Defense": 1.1, "Attack": 0.9}, 
      "Careful": {"Special Defense": 1.1, "Special Attack": 0.9}, 
      "Gentle": {"Special Defense": 1.1, "Defense": 0.9}, 
      "Sassy": {"Special Defense": 1.1, "Speed": 0.9}
      }

    possible_xp_groups = ("Fast", "Medium Fast", "Medium Slow", "Slow", "Erratic", "Fluctuating")

    #Init and Setup, Roll Random IVs for the pokemon
    def __init__(self, name: str, base_total_stat: int = 999, xp_category: str = "Medium Slow", xp_yield: int = 0, nature: str = possible_nature[random.randint(0, len(possible_nature) - 1)]):
        
        #Status Inflicted:
        self.status = []
        self.accuracy = 100
        self.evasion = 100
        self.type = None

        #Level and XP Calculation

        self.xp_category = xp_category
        self.level = 1
        self.max_xp = 0
        self.current_xp = 0


        #Yields Stats:
        self.xp_yield = xp_yield
        self.EV_yield = {"Health": 0, "Attack": 0, "Special Attack": 0, "Defense": 0, "Special Defense": 0, "Speed": 0}

        #Name and Nature of the Pokemon
        self.nature = nature
        
        self.nick_name = name
        self.name = name
        self.possible_ability = {}
        self.ability = None
        self.possible_gender = []
        self.gender = None
        self.base_friendship = 0
        
        #Skill list of the Pokemons
        self.learnable_skill = {}
        self.skill = []

        self.next_evolution = None
        
        #Initiate the Stats, After and Before IVs, Evs, and Final in combat stat
        self.total_stat = base_total_stat

        self.base_stat = {"Health": 0, "Attack": 0, "Special Attack": 0, "Defense": 0, "Special Defense": 0, "Speed": 0}

        self.IV = {"Health": 0, "Attack": 0, "Special Attack": 0, "Defense": 0, "Special Defense": 0, "Speed": 0}

        self.EV = {"Health": 0, "Attack": 0, "Special Attack": 0, "Defense": 0, "Special Defense": 0, "Speed": 0}

        self.nature_mod = {"Attack": 1, "Special Attack": 1, "Defense": 1, "Special Defense": 1, "Speed": 1}

        self.final_stat = {
          
          "Health": int((((2 * self.base_stat["Health"] + self.IV["Health"] + ((self.EV["Health"])/4)) * self.level)/100) + self.level + 10), 

          "Attack": int((int(((2 * self.base_stat["Attack"] + self.IV["Attack"] + (self.EV["Attack"]/4)) * self.level) / 100) + 5) * self.nature_mod["Attack"]), 

          "Special Attack": int((int(((2 * self.base_stat["Special Attack"] + self.IV["Special Attack"] + (self.EV["Special Attack"]/4)) * self.level) / 100) + 5) * self.nature_mod["Special Attack"]), 

          "Defense": int((int(((2 * self.base_stat["Defense"] + self.IV["Defense"] + (self.EV["Defense"]/4)) * self.level) / 100) + 5) * self.nature_mod["Defense"]), 

          "Special Defense": int((int(((2 * self.base_stat["Special Defense"] + self.IV["Special Defense"] + (self.EV["Special Defense"]/4)) * self.level) / 100) + 5) * self.nature_mod["Special Defense"]), 

          "Speed": int((int(((2 * self.base_stat["Speed"] + self.IV["Speed"] + (self.EV["Speed"]/4)) * self.level) / 100) + 5) * self.nature_mod["Speed"])
          
        }

        self.set_IV()
        self.refresh_nature_mod()
        self.set_max_xp()

        self.current_xp = self.max_xp

    def __repr__(self):
      return (f"{self.name} | {self.nature} | Lvl. {self.level} \nIV: {self.IV}\nNatureMod: {self.nature_mod} \n{self.final_stat}")

    #Refresh each time Final stat formula Parameter (level, IV, EV, Base) is changed, or reset to the Default state
    def refresh_stat(self):
      
      """

      Description: Update the Pokemon Max stat, with parameters being if pokemon evolve, EVs, or IVs Change, etc.
      
      """

      self.final_stat.update({
          
          "Health": int((((2 * self.base_stat["Health"] + self.IV["Health"] + ((self.EV["Health"])/4)) * self.level)/100) + self.level + 10), 

          "Attack": int((int(((2 * self.base_stat["Attack"] + self.IV["Attack"] + (self.EV["Attack"]/4)) * self.level) / 100) + 5) * self.nature_mod["Attack"]), 

          "Special Attack": int((int(((2 * self.base_stat["Special Attack"] + self.IV["Special Attack"] + (self.EV["Special Attack"]/4)) * self.level) / 100) + 5) * self.nature_mod["Special Attack"]), 

          "Defense": int((int(((2 * self.base_stat["Defense"] + self.IV["Defense"] + (self.EV["Defense"]/4)) * self.level) / 100) + 5) * self.nature_mod["Defense"]), 

          "Special Defense": int((int(((2 * self.base_stat["Special Defense"] + self.IV["Special Defense"] + (self.EV["Special Defense"]/4)) * self.level) / 100) + 5) * self.nature_mod["Special Defense"]), 

          "Speed": int((int(((2 * self.base_stat["Speed"] + self.IV["Speed"] + (self.EV["Speed"]/4)) * self.level) / 100) + 5) * self.nature_mod["Speed"])
          
        })

    #Set a pokemon Base Stat
    def set_base_stat(self, health = 0, attack = 0, defense = 0, sp_attack = 0, sp_defense = 0, speed = 0):
      total_cost = health + attack + sp_attack + defense + sp_defense + speed

      if total_cost <= self.total_stat:

        self.base_stat["Health"] += health
        self.base_stat["Attack"] += attack
        self.base_stat["Special Attack"] += sp_attack
        self.base_stat["Defense"] += defense
        self.base_stat["Special Defense"] += sp_defense
        self.base_stat["Speed"] += speed
      else:
        print (f"\n\nInsufficient stat points, total cost: {total_cost}, remaining: {self.total_stat}.\n\n")
      self.refresh_stat()
    
    #Set up the Nature so it Reflects on the Pokemon After a Nature is Assign
    def refresh_nature_mod(self):

      if self.nature in self.possible_nature:
        if self.nature in self.neutral_nature:
          return
        elif self.nature in self.nature_mod_list:
          self.nature_mod.update(self.nature_mod_list[self.nature])
      else:
        print("\n\nInvalid Nature, {self.nature}, list of available nature:\n{self.possible_nature}")
      self.refresh_stat()

    #Set specific IVs or Randomize IVs
    def set_IV(self, health = random.randint(0, 31), attack = random.randint(0, 31), defense = random.randint(0, 31), sp_attack = random.randint(0, 31), sp_defense = random.randint(0, 31), speed = random.randint(0, 31)):
      self.IV.update({"Health": health, "Attack": attack, "Special Attack": sp_attack, "Defense": defense, "Special Defense": sp_defense, "Speed": speed})
        
      self.refresh_stat()

    #Calculate XP needed to levelup base on the pokemon Current level
    def set_max_xp(self):
        

        self.max_xp = (int(self.calculate_total_xp(self.level + 1)) - int(self.calculate_total_xp(self.level)))
        if self.xp_category == "Medium Slow":
            if self.level == 1:
                self.max_xp = 9


    #Calculate total xp accumulate up until a level:
    def calculate_total_xp (self, level: int):

      #Set n as next level number to prevent repeat typing
      n = level
      
      singular_xpGroup = {"Fast": int((4 * (n**3)) / 5), "Medium Fast": int(n**3), "Medium Slow": int(((6 * n**3)/5) - (15 * (n ** 2)) + (100 * n) - 140), "Slow": int((5 * (n ** 3))/4)}

      if self.xp_category is None:
        print ("\n\nInputERROR: Attempting to set max_xp to xp_category of value \'None\'\n")
        return
        

      elif self.xp_category in self.possible_xp_groups:

        if self.xp_category in singular_xpGroup:
          return singular_xpGroup[self.xp_category]

        elif self.xp_category is "Erratic":

          if n < 50:
            return int(((n ** 3) * (100 - n))/50)
          elif n >= 50 and n < 68:
            return int(((n ** 3) * (150 - n))/100)
          elif n >= 68 and n < 98:
            return int(((n ** 3) * round((1911 - 10 * (n)) / 3)) / 500)
          elif n >= 98 and n <= 100:
            return int(((n ** 3) * (160 - n))/100)



        elif self.xp_category is "Fluctuating":
          if n < 15:
            return int(((n ** 3) * ((round((n + 1)/3)) + 24)) / 50)  
          elif n >= 15 and n < 36:
            return int(((n ** 3) * (n + 14))/50)
          elif n >= 36 and n <= 100:
            return int(((n ** 3) * (round(n / 2) + 32))/50)
          
        return self.calculate_total_xp(100)

    #Level Up a Pokemon
    def level_up(self):
      if self.level < 100:
        if self.current_xp >= self.max_xp:

          #Set new xp and level up

          self.current_xp -= self.max_xp
          self.level += 1

          self.set_max_xp()
      else:
        print(f"{self.name} is at max level")
      
      self.refresh_stat()
      
    #Allow a Pokemon to gain xp
    def gain_xp(self, front_pokemon: object, enemy: object):
      
      exp_gain = 0 #Total amount of exp gain

      b = enemy.xp_yield #Enemy Pokemon Base XP Yield
      L_e = enemy.level #Enemy Pokemon Current Level
      L_p = front_pokemon.level #Victorious Pokemon, Front line Pokemon current level
      s = 1 #Is the Pokemon receiving this xp the Primary receiver (1 if yes, 2 if no)
      t = 1 #If the Pokemon is Originally owned by the player (1 if yes, 1.5 if no)
      e = 1 #If the Pokemon holding a "Lucky Egg" (1 if not, 1.5 if yes)
      v = 1 #If the winning Pokémon is at or past the level where it would be able to evolve, but it has not. (1.2 if it has not evolve, 1 if otherwise )
      f = 1 #If the Pokemon Friendship is High (220 or more) (1.2 if it is, 1 if Otherwise)

      if self is not front_pokemon:
        s = 2
      
      if self.base_friendship >= 220:
        f = 1.2

      exp_gain = (((b * L_e)/5) * (1/s) * ((((2 * L_e) + 10)/(L_e + L_p + 10)) ** 2.5) + 1) * t * e * v * f

      self.current_xp += exp_gain

      EV_gain = {}

      EV_gain = enemy.get_EV_yield()

      self.gain_EV(EV_gain)
      
      if self.current_xp > self.max_xp:
        self.level_up()

    #Setting Base Friendship of a Pokemon
    def set_base_friendship(self, value):
      self.base_friendship = value
    
    #Set the Base XP yield of Pokemon, this is Change when the pokemon level up
    def set_base_xp_yield(self, value):
      self.xp_yield = value

    #Set the EV Yield of the Pokemon
    def set_EV_yield(self, health:int = 0, attack:int = 0, sp_attack:int = 0, defense:int = 0, sp_defense:int = 0, speed:int = 0):
      self.EV_yield = {"Health": health, "Attack": attack, "Special Attack": sp_attack, "Defense": defense, "Special Defense": sp_defense, "Speed": speed}
    
    #Get the EV yield of the Pokemon
    def get_EV_yield(self) -> dict:
      return self.EV_yield
    
    #Increment the EV of a Pokemon, using a dict as an input:
    def gain_EV(self, EV_dict: dict):
      total = 0
      for key, value in (self.EV).items():
        total += self.EV[key]
      
      remaining = 510 - total

      #Check if The Total EV is greater than 510
      for key, value in EV_dict.items():
        remaining = 510 - total
        if total >= 510:
          return
        #Check if the key exist in the dictionary key of stats
        if key in self.EV.keys():
          #If the EV overdrafts the 510 limit, then add EV
          if value > remaining:
            self.EV.update({key : (self.EV[key] + remaining)})
            total += remaining

            print (f"\nThe pokemon gain {remaining} points in {key}\n")
          else: 
            self.EV.update({key : (self.EV[key] + value)})
            total += self.EV[key]
            print (f"\nThe pokemon gain {value} points in {key}\n")

          #Check if the individual EV stat is over the limit of 252
          if self.EV[key] > 252:
            self.EV[key] = 252
          
          
        else:
          print(f"\nError: No keys, of {key} found in list of EVs Set to Receive\n")
    
      
    def reduce_EV(self, deduct_EV_dict: dict):

      for key, value in deduct_EV_dict.items():
        if deduct_EV_dict[key] in (self.EV).keys():
          (self.EV)[key] -= deduct_EV_dict[key]
          if (self.EV)[key] < 0:
            (self.EV)[key] = 0
          print (f"\nThe Pokemon {key} EV deducted by {value} points.\n")
        else:
          print(f"\nNo such key, existed with the name {key}\n")
    

        
