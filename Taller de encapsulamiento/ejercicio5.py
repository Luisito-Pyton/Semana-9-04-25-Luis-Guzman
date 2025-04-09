class Opcion:
    def __init__(self):
        self.__opcion = ()

    def set_opcion(self, opcion):
        self.__opcion = opcion

    def ejecutar_accion(self):
        return f'Acción ejecutada para la opción: {self.__opcion}'

opcion = Opcion()
opcion.set_opcion('Opción 1')
print(opcion.ejecutar_accion())