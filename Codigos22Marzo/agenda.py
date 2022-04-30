import time
import os

def afenda():
    contactos = {}
    salir = True
    while (salir):
        print('Bienvenido a mi agenda\n')
        print('1.) Ver contactos\n 2.) Agregar contacto\n.3) Buscar contacto\n.4) Modificar contacto\n 5.) Eliminar contacto\n 6.) Salir\n')
        
        opcion = input('igite el numero de la opcion que desea ver: ')
        #os.system('clear')
        if opcion == '1':
            for contacto in contactos:
                for numero in contactos:
                    print('Contacto/Numero')
                    print(numero, contactos[contacto])