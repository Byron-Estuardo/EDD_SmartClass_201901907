class Nodo:
    def __init__(self, curso):
        self.curso = curso
        self.prev = None
        self.next = None

class ListaGrafo:
    def __init__(self):
        self.Cabeza = None
        self.Cola = None
        self.contador = 0

    def get_size(self):
        aux = self.Cabeza
        contadores = 0
        while aux is not None:
            contadores += 1
            aux = aux.next
        return contadores

    def IsEmpty(self):
        if self.Cabeza is None:
            return True
        else:
            return False

    def get_list(self):
        aux = self.Cabeza
        result_list = []
        while aux is not None:
            result_list.append(aux.curso)
            aux = aux.next
        return result_list

    def Insertar(self, curso):
        temp = Nodo(curso)
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

    '''
    for item in lista.iterar()
        print(item)

        busqueda:
        lista.busqueda(dato)
    '''

    def BuscarExiste(self, dato):
        for item in self.iterar():
            valor = item.curso
            if dato == valor.codigo:
                return True
        return False

    def BuscarNodo(self, dato):
        for item in self.iterar():
            valor = item.curso
            if dato == valor.codigo:
                return item