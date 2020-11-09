from robot import get_instrument
from robot import get_operation

def jdbf():
    return get_instrument.all()

x = jdbf()
print(x[0])