palabra = input("Dime una palabra: ")
lista=[]
while palabra != " ":
    lista.append(palabra)
    palabra = input("Dime una palabra: ")
    
buscar = input ("¿Que palabra quieres encontar? ")
print("La he encontrado %d veces"% lista.count(buscar))