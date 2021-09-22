class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Pila:
    def __init__(self):
        self.superior = None

    def apilar(self, dato):
        print(f"Agregando {dato} en la cima de la pila")
        if self.superior == None:
            self.superior = Nodo(dato)
            return
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.superior
        self.superior = nuevo_nodo

    def desapilar(self):
        if self.superior == None:
            print("No hay ningún elemento en la pila para desapilar")
            return

        print(f"Desapilar {self.superior.dato}")
        self.superior = self.superior.siguiente

    def imprimir(self):
        print("Imprimiendo pila:")
        nodo_temporal = self.superior
        while nodo_temporal != None:
            print(f"{nodo_temporal.dato}", end=",")
            nodo_temporal = nodo_temporal.siguiente
        print("")

def print_hi(name):
    print(f'Hi, {name}')
    pila = Pila()
    pila.apilar("Prueba 1")
    pila.apilar("Prueba 2")
    pila.apilar("Prueba 3")
    pila.imprimir()
    pila.desapilar()
    pila.imprimir()
    # pila.apilar("Prueba 44")
    # pila.imprimir()
    #  pila.desapilar()
    # pila.desapilar()
    # pila.imprimir()
    # pila.desapilar()
    # pila.desapilar()
    # pila.imprimir()



if __name__ == '__main__':
    print_hi('PyCharm')

