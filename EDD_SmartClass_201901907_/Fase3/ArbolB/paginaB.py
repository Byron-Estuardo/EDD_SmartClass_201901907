from ArbolB.listaPuntero import listaPuntero
from ArbolB.listaDoble import listaDoble

class paginaB:


    def __init__(self):
        self.puntero = listaPuntero()
        self.datos = listaDoble()
        self.cuenta = 0
        self.maxClaves = 0
        for i in range(0,5):
            if i!= 4:
                self.datos.insertarNodoD("",None,None,None, None)
            self.puntero.insertarPuntero(None)
        self.maxClaves = 5

    def paginaLlena(self):
        return (self.cuenta == self.maxClaves-1)

    def paginaCasiLLena(self):
        return (self.cuenta == self.maxClaves/2)

    def getCodigo(self, posicion):
        return self.datos.devolverDato(posicion).codigo

    def setCodigo(self, posicion, codigo):
        self.datos.insertarDato(codigo, posicion)

    def getNombre(self, posicion):
        return self.datos.devolverDato(posicion).nombre

    def setNombre(self,posicion, nombre):
        self.datos.devolverDato(posicion).nombre = nombre

    def getCreditos(self, posicion):
        self.datos.devolverDato(posicion).creditos

    def setCreditos(self, posicion, creditos):
        self.datos.devolverDato(posicion).creditos = creditos

    def getCodigos(self, posicion):
        self.datos.devolverDato(posicion).codigos

    def setCodigos(self, posicion, codigos):
        self.datos.devolverDato(posicion).codigos = codigos

    def getObligatorio(self, posicion):
        self.datos.devolverDato(posicion).obligatorio

    def setObligatorio(self, posicion, obligatorio):
        self.datos.devolverDato(posicion).obligatorio = obligatorio                        

    def getApuntador(self, posicion):
        return self.puntero.devolverPuntero(posicion).puntero

    def setApuntador(self, posicion, puntero):
        self.puntero.insertarPunteroP(puntero,posicion)