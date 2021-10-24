class Nodo:
    def __init__(self, nombre = None, tareas= None):
        self.nombre = nombre
        self.tareas = tareas
        self.prev = None
        self.next = None


class ListaDobleMeses:
    def __init__(self):
        self.Cabeza = None
        self.Cola = None

    def IsEmpty(self):
        if self.Cabeza is None:
            return True
        else:
            return False

    def Insertar(self, nombre, tareas):
        temp = Nodo(nombre, tareas)
        if self.IsEmpty() == True:
            self.Cabeza = temp
            self.Cola = temp
        else:
            temp.prev = self.Cola
            self.Cola.next = temp
            self.Cola = temp
            # temp.next = self.Cabeza
            # self.Cabeza.prev = temp
            # self.Cabeza = temp

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
            if dato == item.nombre:
                return True
        return False

    def BuscarNodo(self, dato):
        for item in self.iterar():
            if dato == item.nombre:
                return item
        return -1

    def Eliminar(self, dato):
        actual = self.Cabeza
        eliminado = False
        if actual is None:
            eliminado = False
        elif actual.nombre == dato:
            self.Cabeza = actual.next
            self.Cabeza.prev = None
        elif self.Cola.nombre == dato:
            self.Cola = self.Cola.prev
            self.Cola.next = None
            eliminado = True
        else:
            while actual:
                if actual.nombre == dato:
                    actual.prev.next = actual.next
                    actual.next.prev = actual.prev
                    eliminado = True
                actual = actual.next
        if eliminado:
            self.contador -= 1

    '''
    buscar desde elemento y obtener indice
    % (indice, lista[indice])
    '''

    def obtenerIndice(self, dato):
        for item in self.iterar():
            conta = 0
            if dato == item.nombre:
                return conta
            conta += 1
        return -1

    def __getitem__(self, item):
        if item >= 0 and item < self.contador:
            actual = self.Cabeza
            for _ in range(item - 1):
                actual = actual.next
            return actual.nombre
        else:
            raise Exception("Indice no valido. Fuera de Rango")

    '''
    para modificar por medio del indice 
    lista[pos] = nuevo
    '''

    def __setitem__(self, indice, dato):
        if indice >= 0 and indice < self.contador:
            actual = self.Cabeza
            for _ in range(indice - 1):
                actual = actual.next
            actual.nombre = dato
        else:
            raise Exception("Indice no valido. Fuera de Rango")


'''
Lista = ListaDoble()
Lista.insertar()
'''
