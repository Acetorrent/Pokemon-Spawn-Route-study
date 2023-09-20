class pokemon:
  
    possible_nature = ("Adamant", "Bashful", "Brave", "Brave", "Bold", "Calm", "Careful", "Docile", "Gentle", "Hardy", "Hasty", "Impish", "Jolly", "Lax", "Mild", "Modest", "Naive", "Naughty", "Quiet", "Quirky", "Rash", "Relaxed", "Sassy", "Serious", "Timid")
    
    
    def __init__(self, name: str, total_stat: int, nature: str):

        self.nature = nature
        self.name = name
        self.level = 1
        self.total_stat = total_stat
        self.skill = []
        self.base_stats = {"health" : 0, "attack" : 0, "sp attack" : 0, "defense" : 0, "sp defense" : 0, "speed" : 0}
        self.EVs = {}
        self.IVs = {}
        self.final_stat = {}

    def __repr__(self):
        return ("Lvl. {level} | {name}\n".format(level = self.level, name = (self.name).title()))

    def set_stats(self, **values):
        """
        Sample Code
        
        """

        total_cost = 0
        stat_dict = {}

        #Check if the stats entry exist from the stat dictionary

        for key, item in values.items():
            if key in self.base_stats:
                stat_dict[key] = item
            else:
                print (f"Failure to set, {key} does not exist in the list of stats.")
            
        

  