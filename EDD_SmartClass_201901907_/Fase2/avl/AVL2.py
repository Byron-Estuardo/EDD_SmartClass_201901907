class nodo:
    def __init__(self, carne, dpi, nombre, carrera, correo, contra, cred, edad, anos = None):
        self.Carnet = carne
        self.DPI = dpi
        self.Nombre = nombre
        self.Carrera = carrera
        self.Correo = correo
        self.Contra = contra
        self.Creditos = cred
        self.Edad = edad
        self.Anos = anos
        self.izq = None
        self.der = None
        self.altura = 0

class AVL:
    def __init__(self):
        self.raiz = None

    def MAX(self, val1, val2):
        if val1 > val2:
            return val1
        else:
            return val2

    def GetAltura(self, nodo):
        if nodo is None:
            print(nodo.altura)
            return nodo.altura
        else:
            return -1

    def insert(self, carne, dpi, nombre, carrera, correo, contra, cred, edad):
        print("Insert = " + str(carne))
        self.raiz = self.insert_inter(carne, dpi, nombre, carrera, correo, contra, cred, edad, self.raiz)

    def insert_inter(self, carne, dpi, nombre, carrera, correo, contra, cred, edad, raiiz):
        if raiiz is None:
            print("Raiz  = NONE " + str(carne))
            return nodo(carne, dpi, nombre, carrera, correo, contra, cred, edad)
        else:
            print("Else we " + str(carne))
            if carne < raiiz.Carnet:
                raiiz.izq = self.insert_inter(carne, dpi, nombre, carrera, correo, contra, cred, edad, raiiz.izq)
            if self.GetAltura(raiiz.der) - self.GetAltura(raiiz.izq) == -2:
                if carne < raiiz.izq.Carnet:
                    raiiz = self.RI(raiiz)
                else:
                    raiiz = self.RDI(raiiz)
            elif carne > raiiz.Carnet:
                raiiz.der = self.insert_inter(carne, dpi, nombre, carrera, correo, contra, cred, edad, raiiz.der)
                if self.GetAltura(raiiz.der) - self.GetAltura(raiiz.izq) == 2:
                    if carne > raiiz.izq.Carnet:
                        raiiz = self.RD(raiiz)
                    else:
                        raiiz = self.RID(raiiz)
            else:
                raiiz.Carnet = carne
        raiiz.altura = self.MAX(self.GetAltura(raiiz.izq), self.GetAltura(raiiz.der)) + 1
        return raiiz

    def find(self, Carnet):
        if self.raiz is None:
            return None
        else:
            return self._find(Carnet, self.raiz)

    def _find(self, Carnet, raiz):
        if raiz is None:
            return None
        elif Carnet < raiz.Carnet:
            return self._find(Carnet, self.left)
        elif Carnet > raiz.Carnet:
            return self._find(Carnet, self.right)
        else:
            return raiz

    def RI(self, node):
        aux = node.izq
        node.izq = aux.der
        aux.der = node
        node.altura = self.MAX(self.GetAltura(node.izq), self.GetAltura(node.der)) + 1
        aux.altura = self.MAX(self.GetAltura(aux.izq), self.GetAltura(aux.der)) + 1
        return aux

    def RD(self, node):
        aux = node.der
        node.der = aux.izq
        aux.izq = node
        node.altura = self.MAX(self.GetAltura(node.izq), self.GetAltura(node.der)) + 1
        aux.altura = self.MAX(self.GetAltura(aux.izq), self.GetAltura(aux.der)) + 1
        return aux

    def RDI(self, node):
        node.izq = self.RD(node.izq)
        return self.RI(node)

    def RID(self, node):
        node.der = self.RI(node.der)
        return self.RD(node)

    def pre_orden(self):
        self.pre_orden_intern(self.raiz)

    def pre_orden_intern(self, raiz):
        if raiz is None:
            print(raiz.Carnet)
            self.pre_orden_intern(raiz.izq)
            self.pre_orden_intern(raiz.der)

    def inOrden(self):
        self.inOrden_intern(self.raiz)

    def inOrden_intern(self, raiz):
        if raiz is None:
            self.inOrden_intern(raiz.izq)
            #print()
            self.inOrden_intern(raiz.der)

    def postOrden(self):
        self.postOrden_intern(self.raiz)

    def postOrden_intern(self, raiz):
        if raiz is None:
            self.postOrden_intern(raiz.izq)
            #print()
            self.postOrden_intern(raiz.der)
#arbol = AVL()


#arbol.insert(25)
#arbol.insert(15)
#arbol.AVL = AVL.AVLAVL = AVL.AVL(30)
#arbol.insert(8)
#arbol.insert(10)
#arbol.insert(5)
#arbol.insert(28)
#arbol.insert(27)
#arbol.insert(40)

#arbol.inorden(arbol.raiz)
#arbol.graficar()
