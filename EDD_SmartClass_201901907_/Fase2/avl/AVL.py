class nodo:
    def __init__(self,dato):
        self.dato = dato
        self.izq = None
        self.der = None
        self.altura = 0

class avl:
    def __init__(self):
        self.raiz = None

    def MAX(self, val1, val2):
        if val1 > val2:
            return val1
        else:
            return val2

    def insert(self, value):
        self.raiz = self.insert_inter(value, self.raiz)

    def altura(self, node):
        if node is None:
            return node.altura

    def insert_inter(self, value, raiiz):
        if raiiz is None:
            return nodo(value)
        else:
            if value < raiiz.dato:
                raiiz.izq = self.insert_inter(value, raiiz.izq)
            if self.altura(raiiz.der) - self.altura(raiiz.izq) == -2:
                if value < raiiz.izq.dato:
                    raiiz = self.RI(raiiz)
                else:
                    raiiz = self.RDI(raiiz)
            elif value > raiiz.dato:
                raiiz.der = self.insert_inter(value, raiiz.der)
                if self.altura(raiiz.der) - self.altura(raiiz.izq) == 2:
                    if value > raiiz.izq.dato:
                        raiiz = self.RD(raiiz)
                    else:
                        raiiz = self.RID(raiiz)
            else:
                raiiz.dato = value
        raiiz.altura = self.MAX(self.altura(raiiz.izq), self.altura(raiiz.der)) + 1
        return raiiz

    def RI(self, node):
        aux = node.izq
        node.izq = aux.der
        aux.der = node
        node.altura = self.MAX(self.altura(node.izq), self.altura(node.der)) + 1
        aux.altura = self.MAX(self.altura(aux.izq), self.altura(aux.der)) + 1
        return aux

    def RD(self, node):
        aux = node.der
        node.der = aux.izq
        aux.izq = node
        node.altura = self.MAX(self.altura(node.izq), self.altura(node.der)) + 1
        aux.altura = self.MAX(self.altura(aux.izq), self.altura(aux.der)) + 1
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
            print(raiz.dato)
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

arbol = avl()

arbol.insert(25)
arbol.insert(15)
arbol.insert(30)
arbol.insert(8)
arbol.insert(10)
arbol.insert(5)
arbol.insert(28)
arbol.insert(27)
arbol.insert(40)

arbol.inorden(arbol.raiz)
#arbol.graficar()
