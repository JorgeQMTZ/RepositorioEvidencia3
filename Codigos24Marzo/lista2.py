precios = {"manzana": 2, "naranja": 1.5, "platano": 4, "piña": 3}
while True:
    fruta = input ("Dime la fruta que has vendido: ")
    if fruta.lower() not in precios:
        print("Fruta no existe.")
    else:
        cantidad = int(input("Dime la cantidad de fruta que has vendido: "))
        print("el precio de la fruta es de %f" % (cantidad * precios[fruta]))
    opcion = input("Quieres vender otra fruta, escribe s si estas de acerdo, n si no: ")
    while opcion.lower() != "s" and opcion.lower() !="n":
        opcion = input("¿Quieres vender otra fruta, escribe s si etas de acuero, n i no: ")
    if opcion.lower() == "n":
        break
    