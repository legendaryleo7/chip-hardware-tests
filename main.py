from sous_vide_multi_platform import SousVide
from sous_vide_multi_platform import ThermalUnits


sousvide = SousVide(ThermalUnits.FAHRENHEIT)
try :
    sousvide.run()

except KeyboardInterrupt:
    
    import CHIP_IO.Utilities as UT

    UT.unexport_all()
