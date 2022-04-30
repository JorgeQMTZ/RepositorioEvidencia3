alumnos = {}
cantidad = int(input("introduce la cantidad de alumnos que vamos a guardar: "))
for num in range (cantidad):
    alumno = input("Nombre del alumno: ")
    while alumno in alumnos:
        print("Alumno ya existe")
        alumno = input("Nombre del alumno: ")
    notas=[]
    nota = int(input("Dame una nota del alumno (para finalizar introduce una nota negativa): "))
    while nota > 0:
        notas.append(nota)
        nota = int(input("Dame una nota del alumno (para finalizar introduce una nota negativa): "))
    alumnos[alumno] = notas.copy()
    
for alumno, notas in alumnos.items():
    print("%s ha sacado de nota media %f" % (alumno, sum(notas)/len(notas)))
    