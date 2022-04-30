#EJERCICIO2

def linearSearch(item, my_list):
    found = False
    position = 0
    while position < len(my_list) and not found:
        if my_list[position] == item:
            found = True
        position = position + 1
    return found

bag = ['libro', 'lapiz', 'pluma', 'libreta', 'marcador', 'regla']
item = input('¿Que articulo quieres revisar en la mochila?  ')
itemFound = linearSearch(item, bag)
if itemFound:
    print('Si, el articulo esta en la mochia')
else:
    print('No, el articulo no esta en la mochila')
