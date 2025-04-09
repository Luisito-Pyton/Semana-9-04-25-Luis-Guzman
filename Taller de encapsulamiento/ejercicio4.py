class Factura:
    def __init__(self):
        self.__productos = []

    def agregar_producto(self, producto, precio):
        self.__productos.append((producto, precio))

    def calcular_total(self):
        total = sum(precio for _, precio in self.__productos)
        iva = total * 0.19
        return total + iva


factura = Factura()
factura.agregar_producto('Producto A', 100)
factura.agregar_producto('Producto B', 200)
print(f'Total con IVA: {factura.calcular_total()}')