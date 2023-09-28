import pokemon


totodile = pokemon.pokemon("Totodile", 314, "Medium Slow")
_totodile = pokemon.pokemon("Totodile", 314, "Medium Slow")

totodile.set_base_stat(50, 65, 64, 44, 48, 43)
totodile.set_EV_yield(1, 1, 1, 1, 1, 1)

_totodile.set_base_stat(50, 65, 64, 44, 48, 43)
_totodile.set_EV_yield(252, 252, 255, 1, 1, 1)

totodile.gain_xp(totodile, _totodile)

print (totodile.EV)