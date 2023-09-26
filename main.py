import pokemon



totodile = pokemon.pokemon("Totodile", 314, "Fluctuating")

totodile.set_base_stat(50, 65, 64, 44, 48, 43)

for i in range(1, 101):
  totodile.level = i
  totodile.set_max_xp()

  print (f"{totodile.level} {totodile.max_xp}")
  #print (f"{totodile.current_xp}/{totodile.max_xp}")




