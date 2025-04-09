class Estudiante:
    def __init__(self, nombre, notas):
        self.__nombre = nombre
        self.__notas = notas 

    def mostrar_datos(self):
        return f'Nombre: {self.__nombre}, Notas: {self.__notas}'

# Crear 3 objetos Estudiante
estudiante1 = Estudiante('Juan', [85, 90, 78])
estudiante2 = Estudiante('Ana', [92, 88, 95])
estudiante3 = Estudiante('Luis', [75, 80, 70])

# Mostrar datos
print(estudiante1.mostrar_datos())
print(estudiante2.mostrar_datos())
print(estudiante3.mostrar_datos())