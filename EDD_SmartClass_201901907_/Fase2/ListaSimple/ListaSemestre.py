class NodoSemestre:
    def __init__(self,nombres, cursos):
        self.nombre = nombres
        self.curso = cursos
        self.siguiente = None

    def GetNombre(self):
        return self.nombre

    def GetCurso(self):
        return self.curso

    def GetSiguiente(self):
        return self.siguiente

    def SetNombre(self,nombres):
        self.nombre = nombres

    def SetNombre(self,cursos):
        self.curso = cursos

    def SetSiguiente(self,nuevosiguiente):
        self.siguiente = nuevosiguiente

class ListaSemestre:
    def __init__(self):
        self.Cabeza = None

    def IsEmpty(self):
        return self.cabeza == None

    def Insertar(self, nombre, cursos):
        nuevo = NodoSemestre(nombre, cursos)
        nuevo.SetSiguiente(self.Cabeza)
        self.Cabeza = nuevo

    def Tamano(self):
        actual = self.Cabeza
        contador = 0
        while actual != None:
            contador = contador + 1
            actual = actual.GetSiguiente()
        return contador

    def Buscar(self, item):
        actual = self.Cabeza
        encontrado = False
        while actual != None and not encontrado:
            if actual.GetNombre() == item:
                encontrado = True
            else:
                actual = actual.GetSiguiente()

        return encontrado

    def Eliminar(self, item):
        actual = self.Cabeza
        Prev = None
        encontrado = False
        while not encontrado:
            if actual.GetNombre() == item:
                encontrado = True
            else:
                Prev = actual
                actual = actual.GetSiguiente()

        if Prev == None:
            self.Cabeza = actual.GetSiguiente()
        else:
            Prev.SetSiguiente(actual.GetSiguiente())
