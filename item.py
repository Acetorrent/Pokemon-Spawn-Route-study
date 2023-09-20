class item:
  status_list = ("Frozen", "Sleep", "Confusion", "Burn", "Poison", "Badly Poison", "Paralyze", "Disabled")


  class recovery:
    def __init__(self, name: str , HP_recovery: int = 0, PP_recovery: int = 0):
      self.name = name
      self.HP_recovery = HP_recovery
      self.PP_recovery = PP_recovery
      self.status_recovery = []

    def add_status_recovery(self, value: str):
      for item in status_list:
        if value is item:
          self.status_recovery.append(value)
          print(f"{self.name}, will now cure {value}")


    def use(self, user):
      list_attribute = self.__dict__

      for key, value in list_attribute.items():
        if key is "HP_recovery" and value > 0:
          user.heal(value)
        elif key is "PP_recovery" and value > 0:
          user.heal_pp(value)
        elif key is "status_recovery" and len(value) > 0:
          user.heal_status(value)


potion = item.recovery("potion", 10, 5)

