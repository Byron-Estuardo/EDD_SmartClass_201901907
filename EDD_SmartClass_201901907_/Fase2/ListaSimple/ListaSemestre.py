class NodoSemestre:

    def __init__(self,nombres, cursos):
        self.nombre = nombres
        self.curso = cursos
        self.siguiente = None

class ListaSemestre:
    def __init__(self):
        self.Cabeza = None

    def IsEmpty(self):
        return self.cabeza == None

    def Insertar(self, nombre, cursos):
        nuevo = NodoSemestre(nombre, cursos)
        nuevo.siguiente = self.Cabeza
        self.Cabeza = nuevo

    def Tamano(self):
        actual = self.Cabeza
        contador = 0
        while actual != None:
            contador = contador + 1
            actual = actual.siguiente
        return contador

    def Buscar(self, item):
        actual = self.Cabeza
        encontrado = False
        if self.IsEmpty() is not None:
            while actual is not None:
                if actual.nombre == item:
                    print("Dato encontrado" + str(item))
                    encontrado = True
                actual = actual.siguiente
        else:
            print("Lista Vacia")
        if encontrado is False:
            print("Dato No Encontrado")
        return encontrado

    def modificar(self, dato,nuevo):
        auxiliar = self.Cabeza
        if self.Buscar(dato) != 0:
            while auxiliar is not None:
                if auxiliar.nombre == dato:
                    auxiliar.nombre = nuevo
                    print("Dato modificado")
                auxiliar = auxiliar.siguiente
        else:
            print("No se encuentra el dato")

    def Eliminar(self, item):
        actual = self.Cabeza
        Prev = None
        encontrado = False
        while not encontrado:
            if actual.nombre == item:
                encontrado = True
            else:
                Prev = actual
                actual = actual.siguiente

        if Prev is None:
            self.Cabeza = actual.siguiente
        else:
            Prev.siguiente = actual.siguiente

    def lista( self ):
        i = self.Cabeza
        while i is not None:
            if i.siguiente is not None:
                print(i.nombre, end =" => ")
            else:
                print(i.nombre, end =" => NULL")
                print()
            i = i.siguiente
