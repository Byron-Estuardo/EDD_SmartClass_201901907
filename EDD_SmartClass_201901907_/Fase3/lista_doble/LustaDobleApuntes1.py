class Nodo:
    def __init__(self, carne, title, body):
        self.carnet = carne
        self.titulo = title
        self.cuerpo = body
        self.prev = None
        self.next = None


class ListaDoble:
    def __init__(self):
        self.Cabeza = None
        self.Cola = None
        self.contador = 0

    def IsEmpty(self):
        if self.Cabeza is None:
            return True
        else:
            return False

    def Insertar(self, carne, title, body):
        temp = Nodo(carne, title, body)
        if self.IsEmpty() is True:
            self.Cabeza = temp
            self.Cola = temp
        else:
            temp.prev = self.Cola
            self.Cola.next = temp
            self.Cola = temp
            # temp.next = self.Cabeza
            # self.Cabeza.prev = temp
            # self.Cabeza = temp
        self.contador += 1

    def iterar(self):
        actual = self.Cabeza
        while actual:
            dato = actual
            actual = actual.next
            yield dato

    def BuscarExiste(self, dato):
        for item in self.iterar():
            if dato == item.titulo:
                return True
        return False

    def BuscarNodo(self, dato):
        for item in self.iterar():
            if dato == item.titulo:
                return item
        return -1

    def Eliminar(self, dato):
        actual = self.Cabeza
        eliminado = False
        if actual is None:
            eliminado = False
        elif actual.titulo == dato:
            self.Cabeza = actual.next
            self.Cabeza.prev = None
        elif self.Cola.titulo == dato:
            self.Cola = self.Cola.prev
            self.Cola.next = None
            eliminado = True
        else:
            while actual:
                if actual.titulo == dato:
                    actual.prev.next = actual.next
                    actual.next.prev = actual.prev
                    eliminado = True
                actual = actual.next
        if eliminado:
            self.contador -= 1


    def obtenerIndice(self, dato):
        for item in self.iterar():
            conta = 0
            if dato == item.titulo:
                return conta
            conta += 1
        return -1

    def __getitem__(self, item):
        if item >= 0 and item < self.contador:
            actual = self.Cabeza
            for _ in range(item - 1):
                actual = actual.next
            return actual.titulo
        else:
            raise Exception("Indice no valido. Fuera de Rango")

    def __setitem__(self, indice, dato):
        if indice >= 0 and indice < self.contador:
            actual = self.Cabeza
            for _ in range(indice - 1):
                actual = actual.next
            actual.titulo = dato
        else:
            raise Exception("Indice no valido. Fuera de Rango")
