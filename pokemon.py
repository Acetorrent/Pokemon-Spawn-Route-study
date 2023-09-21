class pokemon:
  
    possible_nature = ("Adamant", "Bashful", "Brave", "Brave", "Bold", "Calm", "Careful", "Docile", "Gentle", "Hardy", "Hasty", "Impish", "Jolly", "Lax", "Mild", "Modest", "Naive", "Naughty", "Quiet", "Quirky", "Rash", "Relaxed", "Sassy", "Serious", "Timid")
    possible_xp_groups = ("Fast", "Medium Fast", "Medium Slow", "Slow")
    
    def __init__(self, name: str, total_stat: int, nature: str):

        #Name and Nature of the Pokemon
        self.nature = nature
        self.name = name
        self.ability = None
        self.gender = None
        
        #Skill list of the Pokemons
        self.learnable_skill = []
        self.skill = []
        
        #Initiate the Stats, After and Before IVs, Evs, and Final in combat stat
        self.total_stat = total_stat
        self.base_stats = {"health" : 0, "attack" : 0, "sp attack" : 0, "defense" : 0, "sp defense" : 0, "speed" : 0}
        self.EVs = {"health" : 0, "attack" : 0, "sp attack" : 0, "defense" : 0, "sp defense" : 0, "speed" : 0}
        self.IVs = {"health" : 0, "attack" : 0, "sp attack" : 0, "defense" : 0, "sp defense" : 0, "speed" : 0}

        #Max Base Stat Value
        self.final_stat = {"health" : 0, "attack" : 0, "sp attack" : 0, "defense" : 0, "sp defense" : 0, "speed" : 0}
        #Mutable Base Stat in Battle That will need to be reset after
        self.mutable_stat = {"health" : 0, "attack" : 0, "sp attack" : 0, "defense" : 0, "sp defense" : 0, "speed" : 0}
        #Status Inflicted:
        self.status = None


        #Level and XP Calculation
        self.level = 1
        self.max_xp = 0
        self.current_xp = 0

    def get_skill(self):
        return self.skill

    def __repr__(self):
        return ("Lvl. {level} | {name}\n".format(level = self.level, name = (self.name).title()))

    def heal(self, amount: int):
        if (amount > 0 and amount <= (self.final_stat["health"] - self.mutable_stat["health"])):
            self.mutable_stat["health"] += amount
            value = amount
            if ((self.mutable_stat["health"]) > self.final_stat["health"]):
                value = self.final_stat["health"] - self.mutable_stat["health"]
                self.mutable_stat["health"] = self.final_stat["health"]
        
            print(f" {self.name} healed for {value} HP.")
            

        else:
            print(f"{self.name}'s Health is full!")

    def heal_pp(self, skill, amount: int):
        #Add in the heal PP Function After you add in the Class Skills
        pass

        


            
        

  