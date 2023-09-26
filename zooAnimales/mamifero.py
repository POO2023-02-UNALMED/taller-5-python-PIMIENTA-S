from zooAnimales.animal import Animal


class Mamifero(Animal):
    _listado = []
    caballos = 0
    leones = 0

    def __init__(self, nombre, edad, habitat, genero, pelaje = False, patas = 0):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        self._listado.append(self)

    @staticmethod
    def cantidadMamiferos():
        return len(Mamifero._listado)

    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        cls(nombre, edad, "pradera", genero, True, 4)
        cls.caballos += 1


    @classmethod
    def crearLeon(cls, nombre, edad, genero):
        cls(nombre, edad, "selva", genero, True, 4)
        cls.leones += 1

    def setListado(listado):
        Mamifero._listado = listado

    @staticmethod
    def getListado():
        return Mamifero._listado

    def setPelaje(self, pelaje):
        self._pelaje = pelaje

    def isPelaje(self):
        return self._pelaje

    def setPatas(self, patas):
        self._patas = patas

    def getPatas(self):
        return self._patas