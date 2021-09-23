'_insertar(self.raiz, codigo, nombre, creditos, codigos, obligatorio)'

class paginaB:

    def __init__(self):
        self.raiz = paginaB()
        self.Codigo = 0
        self.Nombre = ""
        self.Creditos = 0
        self.Codigos = 0
        self.Obligatorio = False
        self.aux1 = False
        self.aux2 = paginaB()
        self.sube = False
        self.estado = False
        self.comparador = False
        self.grafica = ""
        self.grafica2 = ""
        self.nombre = ""
        self.nodos = 0

    def estaVacio(self, raiz):
        return (raiz is None or raiz.cuenta == 0)

