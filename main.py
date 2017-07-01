from sous_vide_multi_platform import SousVide
from sous_vide_multi_platform import ThermalUnits


sousvide = SousVide(ThermalUnits.FAHRENHEIT)
sousvide.run()