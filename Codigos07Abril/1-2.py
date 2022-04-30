import csv

class Contacto:
    def __init__(self,USUARIO,NOMBRE,CORREO):
        self.USUARIO = USUARIO
        self.NOMBRE = NOMBRE
        self.CORREO = CORREO
        
Contactos = []

with open('contactos.csv', newline='') as archivo_csv:
    lector_csv = csv.reader(archivo_csv, delimiter='|')
    for e in lector_csv:
        Contactos.append(Contacto(e[0],e[1],e[2]))

for o in Contactos:
    print(o.USUARIO)
    print(o.NOMBRE)
    print(o.CORREO)