class item:
  


  class recovery:
    def __init__(self, name: str , HP_recovery: int = 0, PP_recovery: int = 0):
      self.name = name
      self.HP_recovery = HP_recovery
      self.PP_recovery = PP_recovery
      self.status_recovery = []

    def add_status_recovery(self, value: str):
      status_list = ("Frozen", "Sleep", "Confusion", "Burn", "Poison", "Badly Poison", "Paralyze", "Disabled")
      for item in status_list:
        if value is item:
          self.status_recovery.append(value)
          print(f"{self.name}, will now cure {value}")


    def use(self, user):
      list_attribute = self.__dict__


      for key, value in list_attribute.items():

        #HP Recovery
        if key is "HP_recovery" and value > 0:
          user.heal(value)


        #PP Recovery Check
        elif key is "PP_recovery" and value > 0:
          for item in user.get_skill():
            print (item + "\n")
          skill = input(str("\n\nChoose A Skill to recover!\n\n"))

          skill.strip(" ")
          skill = skill.title()

          for item in user.get_skill():
            if skill is item:
              user.heal_pp(skill, value)

        #Status Recovery
        elif key is "status_recovery" and len(value) > 0:
          user.heal_status(value)



