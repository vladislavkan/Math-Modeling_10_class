import const
from const import g
#g=9.81
def E (mass=1,h=1,V=1):
    """ фуккция определяет полную механническую энергию
    тела массой mass, высотой над Землей h, и скоростью тела V
    """
    F=mass*g*h + mass*V**2/2
    print(F, 'Дж')    
E(50,200,3)
