#EJEMPLO3

import operator

GUITARRISTAS = [
    {'nombre':'Timo', 'apellido':'Tolski', 'banda':'stratovarius'},
    {'nombre':'Eric', 'apellido':'Clapton', 'banda':'Cream'},
    {'nombre':'Eddie', 'apellido':'Van Halen', 'banda':'Van Halen'},
    ]

def ordenarXApellido(GUITARRISTAS):
    return sorted(GUITARRISTAS, key=operator.itemgetter('apellido','nombre'))

print (ordenarXApellido(GUITARRISTAS))