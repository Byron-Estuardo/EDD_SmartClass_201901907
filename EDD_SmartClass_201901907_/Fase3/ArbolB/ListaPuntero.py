class nodoPuntero:
    anteriorP = None
    def __init__(self, puntero):
        self.puntero = puntero
        self.siguienteP = None


class ListaPunteros:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.cuenta = 0

    def estaVacio(self):
        return self.primero is None

    def insertarP(self, puntero):
        nuevo = nodoPuntero(puntero)
        if self.cuenta < 5:
            if self.estaVacio():
                self.primero = nuevo
                self.ultimo = self.primero
            else:
                self.ultimo.siguienteP = nuevo
                nuevo.anteriorP = self.ultimo
                self.ultimo = nuevo
            self.cuenta += 1

    def insertarPunteroP(self, pagina, posicion):
        aux = self.primero
        while(posicion != 0):
            posicion = posicion - 1
            aux = aux.siguienteP
        aux.puntero = pagina

    def devolverPuntero(self, posicion):
        aux = self.primero
        while(posicion != 0):
            posicion = posicion - 1
            aux = aux.siguienteP
        return aux
