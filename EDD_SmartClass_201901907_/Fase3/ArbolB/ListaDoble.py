from ArbolB.nodoDoble import nodoDoble

class listaDoble:
    def __init__(self):
        self.cuenta = 0
        self.primero = None
        self.ultimo = None

    def estaVacio(self):
        return self.primero is None

    def insertarNodoD(self, codigo, nombre, creditos, codigos, obligatorio):
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

    def insertarDato(self, codigo, posicion):
        aux = self.primero
        while(posicion != 0):
            posicion = posicion -1
            aux = aux.siguiente
        aux.codigo = codigo

    def devolverDato(self, posicion):
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