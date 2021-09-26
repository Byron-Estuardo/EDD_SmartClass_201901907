class Nodo:
    def __init__(self, nombre = None, tareas= None):
        self.nombre = nombre
        self.tareas = tareas
        self.prev = None
        self.next = None

    def GetNombre(self):
        return self.nombre

    def GetSemestres(self):
        return self.tareas

    def GetSiguiente(self):
        return self.next

    def GetAnterior(self):
        return self.prev

    def SetNombre(self, nombres):
        self.nombre = nombres

    def SetSemestres(self, nombres):
        self.tareas = nombres

    def SetSiguiente(self, siguiente):
        self.next = siguiente

    def SetAnterior(self, anterior):
        self.prev = anterior


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

    def imprimirPrimero(self):
        print("*******")
        temp = self.Cabeza
        while temp != None:
            print(temp.GetNombre(), end='  ')
            temp = temp.next

    def DeletePrimero(self):
        if self.IsEmpty() == False:
            self.Cabeza = self.Cabeza.next
            self.Cabeza.prev = None

    def DeleteUltimo(self):
        if self.Cola.prev is None:
            self.Cabeza = None
            self.Cola = None
        else:
            self.Cola = self.Cola.prev
            self.Cola.next = None

    def DeletePos(self, pos):
        anterior = self.Cabeza
        actual = self.Cabeza
        k = 0
        if pos > 0:
            while k != pos and actual.next != None:
                anterior = actual
                actual = actual.next
                k += 1
            if k == pos:
                temp = actual.next
                anterior.next = actual.next
                temp.prev = anterior

    def search(self, nombre):
        aux = self.Cabeza
        contador = 0
        while aux:
            if aux.Nombre == nombre:
                # return True
                return contador
            else:
                aux = aux.next
                if aux == self.Cabeza:
                    #return False
                    return -1
            contador += 1


'''
Lista = ListaDoble()
Lista.insertar()
'''
