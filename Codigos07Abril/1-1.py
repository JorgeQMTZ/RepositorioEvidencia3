import os

class Contacto:
    def __init__(self,USUARIO,NOMBRE,CORREO):
        self.USUARIO = USUARIO
        self.NOMBRE = NOMBRE
        self.CORREO = CORREO
        
Contactos = []
Contactos.append(Contacto('master','Jose Ruiz','jose,ruiz@hotmail.com'))
Contactos.append(Contacto('student','Alma Perez','almitarules@hotmail.com'))

ruta = os.path.abspath(os.getcwd())
archivo_trabajo=ruta+"\\contactos.csv"
archivo_respaldo=ruta+"\\contactos.bak"

if os.path.exists(archivo_trabajo):
    if os.path.exists(archivo_respaldo):
        os.remove(archivo_respaldo)
    
    os.rename(archivo_trabajo, archivo_respaldo)
    
f = open(archivo_trabajo,"w+")
f.write("USUARIO|NOMBRE|CORREO\n")
for elemento in Contactos:
    f.write(f'{elemento.USUARIO}|{elemento.NOMBRE}|{elemento.CORREO}\n')

f.close()