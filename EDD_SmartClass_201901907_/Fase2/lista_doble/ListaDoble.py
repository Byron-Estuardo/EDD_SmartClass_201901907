class Nodo:
    def __init__(self, dato = None, semestre = None, meses = None):
        self.dato = dato
        self.semestre = semestre
        self.meses = meses
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

    def Insertar(self, nombre, meses, semestres):
        temp = Nodo(nombre, meses, semestres)
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
            if dato == item.dato:
                return True
        return False

    def BuscarNodo(self, dato):
        for item in self.iterar():
            if dato == item.dato:
                return item
        return -1

    def Eliminar(self, dato):
        actual = self.Cabeza
        eliminado = False
        if actual is None:
            eliminado = False
        elif actual.dato == dato:
            self.Cabeza = actual.next
            self.Cabeza.prev = None
        elif self.Cola.dato == dato:
            self.Cola = self.Cola.prev
            self.Cola.next = None
            eliminado = True
        else:
            while actual:
                if actual.dato == dato:
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
            if dato == item.dato:
                return conta
            conta += 1
        return -1


    def __getitem__(self, item):
        if item>= 0 and item < self.contador:
            actual = self.Cabeza
            for _ in range(item-1):
                actual = actual.next
            return actual.dato
        else:
            raise Exception("Indice no valido. Fuera de Rango")

    '''
    para modificar por medio del indice 
    lista[pos] = nuevo
    '''

    def __setitem__(self, indice, dato):
        if indice>= 0 and indice < self.contador:
            actual = self.Cabeza
            for _ in range(indice-1):
                actual = actual.next
            actual.dato = dato
        else:
            raise Exception("Indice no valido. Fuera de Rango")

    #def ModificarDato(self, dato):



'''
Lista = ListaDoble()
Lista.insertar()
'''
