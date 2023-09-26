from zooAnimales.animal import Animal

class Reptil(Animal):
    _listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        self._listado.append(self)

    @staticmethod
    def cantidadReptiles():
        return len(Reptil._listado)

    @staticmethod
    def movimiento(self):
        return "reptar"

    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        cls(nombre, edad, "humedal", genero, "verde", 3)
        cls.iguanas += 1

    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        cls(nombre, edad, "jugla", genero, "blanco", 1)
        cls.serpientes += 1

    def setListado(listado):
        Reptil._listado = listado

    @staticmethod
    def getListado():
        return Reptil._listado

    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas

    def getColorEscamas(self):
        return self._colorEscamas

    def setLargoCola(self, largoCola):
        self._largoCola = largoCola

    def getLargoCola(self):
        return self._largoCola