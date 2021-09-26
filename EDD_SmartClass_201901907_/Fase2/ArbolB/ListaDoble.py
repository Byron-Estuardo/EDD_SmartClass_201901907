class nodoDoble:
    def __init__(self, codigo, nombre, creditos, codigos, obligatorio):
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos
        self.codigos = codigos
        self.obligatorio = obligatorio
        self.siguiente = None
        self.anterior = None


class ListaDobles:
    def __init__(self):
        self.cuenta = 0
        self.primero = None
        self.ultimo = None

    def estaVacio(self):
        return self.primero is None

    def insertarNodo(self, codigo, nombre, creditos, codigos, obligatorio):
        nuevo = nodoDoble(codigo, nombre, creditos, codigos, obligatorio)
        if self.cuenta < 4:
            if self.estaVacio():
                self.primero = nuevo
                self.ultimo = self.primero
            else:
                self.ultimo.siguiente = nuevo
                nuevo.anterior = self.ultimo
                self.ultimo = nuevo
            self.cuenta += 1
        else:
            print("Se Supero El Tamaño")

    def InsertarDato(self, codigo, posicion):
        aux = self.primero
        while(posicion != 0):
            posicion = posicion -1
            aux = aux.siguiente
        aux.codigo = codigo

    def DevolverDato(self, posicion):
        aux = self.primero
        while(posicion != 0):
            posicion = posicion-1
            aux = aux.siguiente
        return aux

    def mostrarDatos(self):
        aux =  self.primero
        while aux:
            print("Dato: "+ str(aux.codigo) + " Curso: " + aux.nombre)
            aux = aux.siguiente
