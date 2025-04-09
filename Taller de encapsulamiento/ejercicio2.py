class Pago:
    def __init__(self):
        self.__estado = "Pendiente"
        self.__monto = 0

    def realizar_pago(self, monto):
        self.__monto = monto
        self.__estado = "Completado"

    def mostrar_estado(self):
        return f'Estado: {self.__estado}, Monto: {self.__monto}'


pago = Pago()
pago.realizar_pago(100)
print(pago.mostrar_estado())