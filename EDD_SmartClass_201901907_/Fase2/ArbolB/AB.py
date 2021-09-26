import os
from paginaB import paginaBB

contadorGrafos = 0


class arbolB:
    def __init__(self):
        self.raiz = paginaBB()
        self.Codigo = 0
        self.Nombre = ""
        self.Creditos = 0
        self.Codigos = 0
        self.Obligatorio = False
        self.aux1 = False
        self.aux2 = paginaBB()
        self.sube = False
        self.estado = False
        self.comparador = False
        self.grafica = ""
        self.grafica2 = ""
        self.nombre = ""
        self.nodos = 0

    def estaVacio(self, raiz):
        return (raiz is None or raiz.cuenta == 0)

    def insertarDatos(self, codigo, nombre, creditos, codigos, obligatorio):
        self._insertar(self.raiz, codigo, nombre, creditos, codigos, obligatorio)

    def _insertar(self, raiz, codigo, nombre, creditos, codigos, obligatorio):
        self.empujar(raiz, codigo, nombre, creditos, codigos, obligatorio)
        if self.sube:
            self.raiz = paginaBB()
            self.raiz.cuenta = 1
            self.raiz.setCodigo(0, self.Codigo)
            self.raiz.setNombre(0, self.Nombre)
            self.raiz.setCreditos(0, self.Creditos)
            self.raiz.setCodigos(0, self.Codigos)
            self.raiz.setObligatorio(0, self.Obligatorio)
            self.raiz.setApuntador(0, raiz)
            self.raiz.setApuntador(1, self.aux2)

    def empujar(self, raiz, codigo, nombre, creditos, codigos, obligatorio):
        posicion = 0
        self.estado = False

        if (self.estaVacio(raiz) and self.comparador == False):
            self.sube = True
            self.Codigo = codigo
            self.Nombre = nombre
            self.Creditos = creditos
            self.Codigos = codigos
            self.Obligatorio = obligatorio
            self.aux2 = None
        else:
            posicion = self.buscarNodoB(codigo, raiz)
            if self.comparador == False:
                if self.estado:
                    self.sube = False
                else:
                    self.empujar(raiz.getApuntador(posicion), codigo, nombre, creditos, codigos, obligatorio)
                    if self.sube:
                        if raiz.cuenta < 4:
                            self.sube = False
                            self.MeterHoja(raiz, posicion, self.Codigo, self.Nombre, self.Creditos, self.Codigos,
                                           self.Obligatorio)
                        else:
                            self.sube = True
                            self.DividirPaginaB(raiz, posicion, self.Codigo, self.Nombre, self.Creditos, self.Codigos,
                                                self.Obligatorio)
            else:
                print("Dato Repetido")
                self.comparador = False

    def buscarNodoB(self, codigo, raiz):
        auxContador = 0
        # if len(str(codigo)) - len(str(raiz.getCodigo(0))) < 0:
        if codigo < raiz.getCodigo(0):
            self.comparador = False
            auxContador = 0
        else:
            while (auxContador != raiz.cuenta):
                if codigo == raiz.getCodigo(auxContador):
                    self.comparador = True
                auxContador += 1
            auxContador = raiz.cuenta

            # while(len(str(codigo)) - len(str(raiz.getCodigo(auxContador-1))) < 0 and auxContador > 1):
            while (codigo < raiz.getCodigo(auxContador - 1) and auxContador > 1):
                auxContador -= 1
                self.estado = codigo == raiz.getCodigo(auxContador - 1)

        return auxContador

    def MeterHoja(self, raiz, posicion, codigo, nombre, creditos, codigos, obligatorio):
        auxC = raiz.cuenta
        while (auxC != posicion):
            if (auxC != 0):
                raiz.setCodigo(auxC, raiz.getCodigo(auxC - 1))
                raiz.setNombre(auxC, raiz.getNombre(auxC - 1))
                raiz.setCreditos(auxC, raiz.getCreditos(auxC - 1))
                raiz.setCodigos(auxC, raiz.getCodigos(auxC - 1))
                raiz.setObligatorio(auxC, raiz.getObligatorio(auxC - 1))
                raiz.setApuntador(auxC + 1, raiz.getApuntador(auxC))
            auxC -= 1
        raiz.setCodigo(posicion, codigo)
        raiz.setNombre(posicion, nombre)
        raiz.setCreditos(posicion, creditos)
        raiz.setCodigos(posicion, codigos)
        raiz.setObligatorio(posicion, obligatorio)
        raiz.setApuntador(posicion + 1, self.aux2)
        raiz.cuenta = raiz.cuenta + 1

    def DividirPaginaB(self, raiz, posicion, codigo, nombre, creditos, codigos, obligatorio):
        posicion2 = 0
        posicionMedia = 0
        if posicion <= 2:
            posicionMedia = 2
        else:
            posicionMedia = 3

        paginaDerecha = paginaBB()
        posicion2 = posicionMedia + 1

        while (posicion2 != 5):
            if (posicion2 - posicionMedia) != 0:
                paginaDerecha.setCodigo((posicion2 - posicionMedia) - 1, raiz.getCodigo(posicion2 - 1))
                paginaDerecha.setNombre((posicion2 - posicionMedia) - 1, raiz.getNombre(posicion2 - 1))
                paginaDerecha.setCreditos((posicion2 - posicionMedia) - 1, raiz.getCreditos(posicion2 - 1))
                paginaDerecha.setCodigos((posicion2 - posicionMedia) - 1, raiz.getCodigos(posicion2 - 1))
                paginaDerecha.setObligatorio((posicion2 - posicionMedia) - 1, raiz.getObligatorio(posicion2 - 1))
                paginaDerecha.setApuntador((posicion2 - posicionMedia), raiz.getApuntador(posicion2))
            posicion2 += 1

        paginaDerecha.cuenta = (4 - posicionMedia)
        raiz.cuenta = posicionMedia

        if posicion <= 2:
            self.aux1 = True
            self.MeterHoja(raiz, posicion, codigo, nombre, creditos, codigos, obligatorio)
        else:
            self.aux1 = True
            self.MeterHoja(paginaDerecha, (posicion - posicionMedia), codigo, nombre, creditos, codigos, obligatorio)

        self.Codigo = raiz.getCodigo(raiz.cuenta - 1)
        self.Nombre = raiz.getNombre(raiz.cuenta - 1)
        self.Creditos = raiz.getCreditos(raiz.cuenta - 1)
        self.Codigos = raiz.getCodigos(raiz.cuenta - 1)
        self.Obligatorio = raiz.getObligatorio(raiz.cuenta - 1)

        paginaDerecha.setApuntador(0, raiz.getApuntador(raiz.cuenta))

        raiz.cuenta = raiz.cuenta - 1
        self.aux2 = paginaDerecha

        if self.aux1:
            raiz.setCodigo(3, "")
            raiz.setNombre(3, "")
            raiz.setCreditos(3, "")
            raiz.setCodigos(3, "")
            raiz.setObligatorio(3, "")
            raiz.setApuntador(4, None)

            raiz.setCodigo(2, "")
            raiz.setNombre(2, "")
            raiz.setCreditos(2, "")
            raiz.setCodigos(2, "")
            raiz.setObligatorio(2, "")
            raiz.setApuntador(3, None)



a = arbolB()
a.insertarDatos(100, "MB1", " ", " ", " ")
a.insertarDatos(200, "MB2", " ", " ", " ")
a.insertarDatos(300, "MB3", " ", " ", " ")
a.insertarDatos(400, "MB4", " ", " ", " ")
a.insertarDatos(500, "MB5", " ", " ", " ")
a.insertarDatos(600, "MB6", " ", " ", " ")
a.insertarDatos(700, "MB7", " ", " ", " ")
a.insertarDatos(800, "MB1", " ", " ", " ")
a.insertarDatos(900, "MB2", " ", " ", " ")
a.insertarDatos(1300, "MB3", " ", " ", " ")
a.insertarDatos(1400, "MB4", " ", " ", " ")
a.insertarDatos(1500, "MB5", " ", " ", " ")
a.insertarDatos(1600, "MB6", " ", " ", " ")
a.insertarDatos(1700, "MB7", " ", " ", " ")
a.insertarDatos(2000, "MB5", " ", " ", " ")
a.insertarDatos(2100, "MB6", " ", " ", " ")
a.insertarDatos(2200, "MB7", " ", " ", " ")
a.insertarDatos(2300, "MB6", " ", " ", " ")
a.insertarDatos(2400, "MB7", " ", " ", " ")
#a.graficar()
