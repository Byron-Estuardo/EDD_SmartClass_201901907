class nodoDoble:
    def __init__(self, codigo, nombre, creditos, codigos, obligatorio):
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos
        self.codigos = codigos
        self.obligatorio = obligatorio
        self.siguiente = None
        self.anterior = None