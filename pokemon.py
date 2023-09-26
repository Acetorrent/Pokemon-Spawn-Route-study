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
    def __init__(self, name: str, base_total_stat: int, xp_category: str, nature: str = possible_nature[random.randint(0, len(possible_nature) - 1)]):
        
        #Status Inflicted:
        self.status = []
        self.accuracy = 100
        self.evasion = 100


        #Level and XP Calculation
        if xp_category in self.possible_xp_groups:
          self.xp_category = xp_category
        else:
          self.xp_category = None
          print ("\nERROR: No exp category with name {xp_category} found.\n\n")
        self.level = 1
        self.max_xp = 0
        self.current_xp = 0

        #Name and Nature of the Pokemon
        self.nature = nature
        self.name = name
        self.possible_ability = {}
        self.ability = None
        self.possible_gender = []
        self.gender = None
        self.type = None
        
        #Skill list of the Pokemons
        self.learnable_skill = {}
        self.skill = []
        
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


    def set_max_xp(self):
      self.max_xp = (self.calculate_total_xp(self.level + 1) - self.calculate_total_xp(self.level))


    #Calculate total xp accumulate up until a level:
    def calculate_total_xp (self, level: int):

      #Set n as next level number to prevent repeat typing
      n = level
      
      singular_xpGroup = {"Fast": int((4 * (n**3)) / 5), "Medium Fast": int(n**3), "Medium Slow": int(((6 * n**3)/5) - (15 * (n ** 2)) + (100 * n) - 140), "Slow": int((5 * (n ** 3))/4)}

      if self.xp_category is None:
        return
        print ("\n\nInputERROR: Attempting to set max_xp to xp_category of value \'None\'\n")

      elif self.xp_category in self.possible_xp_groups:

        if self.xp_category in singular_xpGroup:
          return singular_xpGroup[self.xp_category]

        elif self.xp_category is "Erratic":

          if n < 50:
            return int(((n ** 3) * (100 - n))/50)
          elif n >= 50 and n < 68:
            return int(((n ** 3) * (150 - n))/100)
          elif n >= 68 and n < 98:
            return (n ** 3) * int(round((1911 - (10 * n))/3) / 500)
          elif n >= 98 and n < 100:
            return int(((n ** 3) * (160 - n))/100)
          else:
            print (f"\nLvl_OUTBOUND: Level: {n} is out of bound")

        elif self.xp_category is "Fluctuating":
          if n < 15:
            return int(((n ** 3) * ((round((n + 1)/3)) + 24)) / 50)  
          elif n >= 15 and n < 36:
            return int(((n ** 3) * (n + 14))/50)
          elif n >= 36 and n < 100:
            return int(((n ** 3) * (round(n / 2) + 32))/50)
          else:
            print (f"\nLvl_OUTBOUND: Level: {n} is out of bound")

    