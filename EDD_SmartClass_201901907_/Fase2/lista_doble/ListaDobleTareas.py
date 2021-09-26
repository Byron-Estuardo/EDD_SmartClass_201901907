class Nodo:
    def __init__(self, carne= None,nombre= None,descrip= None,materia= None,fecha= None,hora= None,estado= None):
        self.carne = carne
        self.nombre = nombre
        self.descripcion = descrip
        self.materia = materia
        self.fecha = fecha
        self.hora = hora
        self.estado = estado
        self.prev = None
        self.next = None


class ListaDobleTareas:
    def __init__(self):
        self.Cabeza = None
        self.Cola = None

    def IsEmpty(self):
        if self.Cabeza is None:
            return True
        else:
            return False

    def Insertar(self, carne,nombre,descrip,materia,fecha,hora,estado):
        temp = Nodo(carne,nombre,descrip,materia,fecha,hora,estado)
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

    def search(self, nombre, tareas):
        aux = self.Cabeza
        contador = 0
        while aux:
            if aux.Nombre == nombre and aux.tareas == tareas:
                # return True
                return contador
            else:
                aux = aux.next
                if aux == self.Cabeza:
                    # return False
                    return -1
            contador += 1


'''
Lista = ListaDoble()
Lista.insertar()
'''
