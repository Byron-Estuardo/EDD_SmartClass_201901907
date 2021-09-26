from ListaPuntero import ListaPunteros
from ListaDoble import ListaDobles

class paginaBB:

    def __init__(self):
        self.cuenta = 0
        self.maxClaves = 0
        self.punteros = ListaPunteros()
        self.datos = ListaDobles()
        for x in range(0, 5):
            if x != 4:
                self.datos.insertarNodo("", None, None, None, None)
            self.punteros.insertarP(None)
        self.maxClaves = 5

    def paginaLlena(self):
        return (self.cuenta == self.maxClaves - 1)

    def paginaCasiLLena(self):
        return (self.cuenta == self.maxClaves / 2)

    def getCodigo(self, posicion):
        return self.datos.DevolverDato(posicion).codigo

    def setCodigo(self, posicion, codigo):
        self.datos.InsertarDato(codigo, posicion)

    def getNombre(self, posicion):
        return self.datos.DevolverDato(posicion).nombre

    def setNombre(self, posicion, nombre):
        self.datos.DevolverDato(posicion).nombre

    def getCreditos(self, posicion):
        self.datos.DevolverDato(posicion).creditos

    def setCreditos(self, posicion, creditos):
        self.datos.DevolverDato(posicion).creditos = creditos

    def getCodigos(self, posicion):
        self.datos.DevolverDato(posicion).codigos

    def setCodigos(self, posicion, codigos):
        self.datos.DevolverDato(posicion).codigos = codigos

    def getObligatorio(self, posicion):
        self.datos.DevolverDato(posicion).obligatorio

    def setObligatorio(self, posicion, obligatorio):
        self.datos.DevolverDato(posicion).obligatorio = obligatorio

    def getApuntador(self, posicion):
        return self.punteros.devolverPuntero(posicion).puntero

    def setApuntador(self, posicion, puntero):
        self.punteros.insertarPunteroP(puntero, posicion)