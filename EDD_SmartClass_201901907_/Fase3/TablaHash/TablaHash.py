import json
import os
from lista_doble import LustaDobleApuntes1

class Nodo:
    def __init__(self, carnet):
        self.carnet = carnet
        self.apuntes = LustaDobleApuntes1.ListaDoble()

    def insertar(self, title, body):
        self.apuntes.Insertar(self.carnet, title, body)

class TablaHash:
    def __init__(self, valor=7):
        self.vector = []
        self.elementos = 0
        self.factorCarga = 0
        self.tamano = valor

        for i in range(valor):
            self.vector.append(None)

    def obtenerPrimoSiguiente(self,actual):
        EsPrimo = False
        nuevoValorPrimo = actual
        while not EsPrimo:
            nuevoValorPrimo += 1
            x = 0
            i = 1
            for i in range(nuevoValorPrimo + 1):
                if i != 0:
                    if nuevoValorPrimo % i == 0:
                        x += 1
                i += 1
            if x == 2:
                EsPrimo = True
        return nuevoValorPrimo

    def ObtenerApuntes(self, carnet):
        for i in range(0, self.tamano):
            number = (carnet+pow(i, 2)) % self.tamano
            if self.vector[number]:
                if self.vector[number].carnet == carnet:
                    archivo = '[\n'
                    i2 = self.vector[number].apuntes
                    for item in i2.iterar():
                        archivo += "{\n\"titulo\": \"" + item.titulo + "\",\n"
                        archivo += "\"body\": \"" + item.cuerpo + "\"\n},"
                        print(item.titulo + ': ' + item.cuerpo + ',')
                    archivo = archivo[:-1]
                    archivo+="\n]"
                    return json.loads(archivo)

    def EstaOcupado(self,index):
        if not (index>self.tamano):
            if self.vector[index] is None:
                return True
        return False

    def ExploracionCuadratica(self, posicion, carnet):
        a = 0
        for i in range(0, self.tamano):

            respuesta = (posicion + pow(a, 2)) % self.tamano
            if self.EstaOcupado(respuesta):
                return False, (respuesta)

            if self.vector[respuesta].carnet == carnet:
                return True, respuesta
            a += 1

        return False, -1

    def insertar(self, carnet, titulo, cuerpo):
        posicion = self.funcion_hash(carnet)
        if self.EstaOcupado(posicion):
            nuevo = Nodo(carnet)
            nuevo.apuntes.Insertar(carnet, titulo, cuerpo)
            self.vector[posicion] = nuevo
            self.elementos += 1
            self.factorCarga = self.elementos / self.tamano
        else:
            booleano, pos = self.ExploracionCuadratica(carnet % (self.tamano - 1), carnet)
            if booleano == True:
                self.vector[pos].apuntes.Insertar(carnet, titulo, cuerpo)
            else:
                if pos != -1:
                    nuevo = Nodo(carnet)
                    nuevo.apuntes.Insertar(carnet, titulo, cuerpo)
                    self.vector[pos] = nuevo
                    self.elementos += 1
                    self.factorCarga = self.elementos / self.tamano
                else:
                    print("No se pudo insertar")
        if self.factorCarga >= 0.5:
            self.rehashing()



    def rehashing(self):
        siguiente = self.obtenerPrimoSiguiente(self.tamano)
        temporal = []
        self.elementos = 0
        for i in range(siguiente):
            temporal.append(None)

        aux_vector = self.vector

        self.vector = temporal
        self.tamano = siguiente
        for i in aux_vector:
            if i:
                i2 = i.apuntes
                for item in i2.iterar():
                    carnet = item.carnet
                    title = item.titulo
                    body = item.cuerpo
                    self.insertar(carnet, title, body)

    def PrintTable(self):
        print('Tamamo de la tabla = ' + str(self.tamano))
        print('Cantidad de elementos ingresados = ' + str(self.elementos))
        print('Factor de carga = ' + str(self.factorCarga))
        for i in range(self.tamano):
            if self.vector[i]:
                tmp = self.vector[i]

                print(str(i)+'-'+str(tmp.carnet)+': ')
                i2 = tmp.apuntes
                for item in i2.iterar():
                    print(item.titulo + ': ' + item.cuerpo + ',')


    def funcion_hash(self, carnet):
        posicion = carnet % (self.tamano - 1)
        if posicion > self.tamano:
            return posicion - self.tamano
        return posicion

    def reporteTable(self):
        cadena = ''
        cadena += "digraph { \n"
        cadena += "graph [pad=\"0.5\", nodesep=\"0.5\", ranksep=\"2\"]; \nnode [shape=plain] \n rankdir=LR;\n"

        cadena += "table [label=<\n<table border=\"0\" cellborder=\"1\" cellspacing=\"0\">\n"
        t_i = 0
        for i in self.vector:
            if i is None:
                cadena += "<tr><td port=\"" + str(t_i) + "\"> </td></tr>\n"
            else:
                cadena += "<tr><td port=\"" + str(t_i) + "\">" + str(i.carnet) + "</td></tr>\n"
            t_i += 1
        cadena += "</table>>];\n"
        cadena += "node [shape=record]\n"
        t = 0
        c = 0
        for k in self.vector:
            first = True
            if k is not None:
                nuevo = k.apuntes
                for info in nuevo.iterar():
                    cadena += "n_" + str(t) + "[label=\"" + info.titulo + ": " + info.cuerpo + "\"]\n"
                    if not first:
                        cadena += "n_" + str(t - 1) + "-> n_" + str(t) + ";\n"
                    else:
                        cadena += "table:" + str(c) + "->" + "n_" + str(t) + ";\n"
                        first = False
                    t += 1
            c += 1

        cadena += '}'
        reporte_hash = open("TablaApuntes.dot", "w+")
        reporte_hash.write(cadena)
        reporte_hash.close()
        os.system("dot -Tpng -o TablaApuntes.png TablaApuntes.dot ")
'''
tabla = TablaHash()
#201901907 - 3 -
#5469126 - 1
#65198456 - 1
#564 - 1
#5184656864 - 1
#5844464 - 1
#5184 - 1
#6753164 - 1
#84654 - 1
#1111 - 2
tabla.insertar(201901907,'pedro','estaoes una descripcion laocaquissmoa')
tabla.insertar(201901907,'el pedro','estaoes una descripcion laocaquissmoa')

tabla.insertar(5469126,'edro','estaoes una descripcion laocaquissmoa')
tabla.insertar(65198456,'esdro','estaoes una descripcion laocaquissmoa')
tabla.insertar(564,'elo','estaoes una descripcion laocaquissmoa')
tabla.insertar(5184656864,'el pedo','estaoes una descripcion laocaquissmoa')
tabla.insertar(5844464,'o','estaoes una descripcion laocaquissmoa')
tabla.insertar(5184,'o','estaoes una descripcion laocaquissmoa')
tabla.insertar(6753164,'o','estaoes una descripcion laocaquissmoa')
tabla.insertar(201901907,'an','estaoes una descripcion laocaquissmoa')
tabla.insertar(84654,'eo','estaoes una descripcion laocaquissmoa')#

tabla.insertar(1111,'el hola','estaoes una descripcion laocaquissmoa')
tabla.insertar(1111,'el adios','adsfasdjlkasda')
tabla.PrintTable()
tabla.reporteTable()
'''