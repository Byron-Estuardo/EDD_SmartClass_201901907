from lista_doble import ListaGrafo

class NodoGrafo:
    def __init__(self, curso, list_) -> None:
        self.curso = curso
        self.list = list_
        self.prev = None
        self.next = None

class Grafos:
    def __init__(self) -> None:
        self.Cabeza = None
        self.Cola = None

    def get_size(self):
        aux = self.Cabeza
        contadores = 0
        while aux is not None:
            contadores += 1
            aux = aux.next
        return contadores

    def iterar(self):
        actual = self.Cabeza
        while actual:
            dato = actual
            actual = actual.next
            yield dato

    def IsEmpty(self):
        if self.Cabeza is None:
            return True
        else:
            return False

    def BuscarExiste(self, dato):
        for item in self.iterar():
            valor = item.curso
            if dato == valor.codigo:
                return True
        return False

    def BuscarExiste(self, verification_number):
        aux = self.Cabeza
        while aux is not None:
            if aux.curso.codigo == verification_number:
                return True
            aux = aux.next
        return False

    def insert_node(self, curso):
        if not self.BuscarExiste(curso.codigo):
            new_list = ListaGrafo.ListaGrafo()
            new_node = NodoGrafo(curso, new_list)

            if self.IsEmpty() is True:
                self.Cabeza = new_node
                self.Cola = new_node
            else:
                new_node.prev = self.Cola
                self.Cola.next = new_node
                self.Cola = new_node
        else:
            print("el valor ya exite dentro de la lista")

    def link_graph(self, value_1, value_2):
        aux = self.Cabeza
        while aux is not None:
            if aux.curso.codigo == value_1.codigo:
                aux.list.Insertar(value_2)
                break
            aux = aux.next

        # while aux is not None:
        #     if aux.number == value_2:
        #         aux.list.Insertar(value_1)
        #         break
        #     aux =  aux.next

    def get_list(self):
        aux = self.Cabeza
        Counter = 0
        adjacency_list = ""
        while aux is not None:
            if not aux.list.IsEmpty():
                aux2 = aux.list.Cabeza
                while aux2 is not None:
                    adjacency_list += f'-> {str(aux2.curso.codigo)}'
                    aux2 = aux2.next

            print(f'{str(Counter)}) {str(aux.curso.codigo)} : {adjacency_list}')
            adjacency_list = ""
            Counter += 1

            aux = aux.next

    def RecorrerGrafo(self):
        etiqueta = ""
        aux = self.Cabeza

        while aux is not None:

            if not aux.list.IsEmpty():
                aux2 = aux.list.Cabeza
                nodo = "n" + str(aux.curso.codigo)
                etiqueta += "n" + str(aux.curso.codigo) + "[label= \"" "Nombre: " + str(aux.curso.nombre) + "\n" + "Codigo: " + str(
                    aux.curso.codigo) + "\n" + "Creditos: " + str(aux.curso.creditos) + "\n" + "Obligatorio: " + str(aux.curso.obligatorio) + "\"];\n"

                while aux2 is not None:
                    nodo2 = "n" + str(aux2.curso.codigo)
                    etiqueta += nodo2 + "->" + nodo + "\n"
                    nodo2 = ""

                    aux2 = aux2.next

            if aux.list.IsEmpty():
                aux2 = aux.list.Cabeza
                nodo = "n" + str(aux.curso.codigo)

                etiqueta += "n" + str(aux.curso.codigo) + "[label= \"" "Nombre: " + str(aux.curso.nombre) + "\n" + "Codigo: " + str(
                    aux.curso.codigo) + "\n" + "Creditos: " + str(aux.curso.creditos) + "\n" + "Obligatorio: " + str(aux.curso.obligatorio) + "\"];\n"
                while aux2 is not None:
                    nodo2 = "n" + str(aux2.number)

                    etiqueta += nodo2 + "->" + nodo + "\n"
                    nodo2 = ""
                    aux2 = aux2.next

            nodo = ""
            aux = aux.next
        return etiqueta

    def EscribirArchivo(self):
        contenido = self.RecorrerGrafo()
        return "digraph {\n" + "rankdir=\"LR\" \n" + "node[shape = \"box\", style=filled, fillcolor=seashell2]\n" + contenido + "}\n";

    def GraficarPensum(self):
        import os
        f = open('GrafoPensum.dot', 'w+', encoding='utf-8')
        f.write(self.EscribirArchivo())
        f.close()
        os.system('dot -Tpng -o GrafoPensum.png GrafoPensum.dot')

    def GraficarPre(self):
        import os
        f = open('GrafoPre.dot', 'w+', encoding='utf-8')
        f.write(self.EscribirArchivo())
        f.close()
        os.system('dot -Tpng -o GrafoPre.png GrafoPre.dot')
