class Cuenta:
    def __init__(self, usuario, contra):
        self.__usuario = usuario
        self.__contra = contra

    def validar_acceso(self, usuario, contra):
        return usuario == self.__usuario and contra == self.__contra


cuenta = Cuenta('user1', 'pass123')
print(cuenta.validar_acceso('user1', 'pass123')) 