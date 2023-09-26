from zooAnimales.animal import Animal


class Ave(Animal):
    _listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self.colorPlumas = colorPlumas
        self._listado.append(self)

    def getColorPlumas(self):
        return self._colorPlumas

    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas

    def getListado(self):
        return self._listado

    def setListado(self, listado):
        self._listado = listado

    @staticmethod
    def cantidadAves():
        return len(Ave._listado)

    def getHabitat(self):
        return super().getHabitat()

    @staticmethod
    def movimiento():
        return "volar"

    @staticmethod
    def crearHalcon(nombre, edad, genero):
        colorPlumas = "cafe glorioso"
        habitat = "montanas"
        Ave(nombre, edad, habitat, genero, colorPlumas)
        Ave.halcones += 1

    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        cls(nombre, edad, "montaña", genero, "blanco y amarillo")
        cls.aguilas += 1
