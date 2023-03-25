class estudiante:
    def __init__(self):
        self.nombre = ""
        self.apellido = ""
        self.edad = 10
    def verificarEdad(self):
        print("La edad del usuario es : ")
        print(str(self.edad))

est1 = estudiante()

est1.nombre = "Alexander"
est1.apellido = "Segovia"
est1.edad = 25

print("Imprimiendo los datos del estudiante 1")
print(est1.nombre)
print(est1.apellido)
print(str(est1.edad))

est2 = estudiante()
est2.nombre = "Diego"
est2.apellido = "Diaz"
est2.edad = 28

print("Imprimiendo los datos del estudiante 2")
print(est2.nombre)
print(est2.apellido)
print(str(est2.edad))

print("Imprimiendo los tipos de variable de est1 y est2")
print(type(est1))
print(type(est2))

lista_estudiantes = [est1,est2]

print("Se imprimen los nombre de los estudiantes creados")
for alumno in lista_estudiantes:
    print(alumno.nombre)

est1.verificarEdad()
est2.verificarEdad()