class Nodo:
    def __init__(self, data=None, siguiente=None):
        self.data = data
        self.siguiente = siguiente


class Lista:
    POSICION_NO_VALIDA = IndexError('la posicion ingresada no es valida')
    ELEMENTO_NO_ENCONTRADO = ValueError(
        'El elemento no se encuentra en la lista')

    def __init__(self, *elementos):
        """
        Crea una lista con los elementos pasados
        """
        self.frente = Nodo()
        self.tamanio = 0
        self.__ultimo__ = self.frente

        for elemento in elementos:
            self.insert(elemento)

    def __len__(self):
        """Return len(self)."""
        return self.tamanio

    def __get_nodo(self, posicion):
        if (posicion < 0) or (posicion >= len(self)):
            raise self.POSICION_NO_VALIDA
        else:
            actual = self.frente
            for i in range(0, posicion + 1):
                actual = actual.siguiente
            return actual

    def insert(self, elemento, posicion=None):
        """
        Inserta el elemento "elemento" en la posicion "posicion" pasando los
        elementos de "posicion" y posteriores un casillero hacia adelante
        Si se omite "posicion" el elemento es insertado al final de la lista
        """
        if posicion == None:
            posicion = len(self)
        elif posicion < 0:
            posicion = len(self) + posicion

        if (posicion > len(self)) or posicion < 0:
            raise self.POSICION_NO_VALIDA

        aux = Nodo(elemento)
        if posicion == len(self):
            self.__ultimo__.siguiente = aux
            self.__ultimo__ = aux
        elif posicion == 0:
            aux.siguiente = self.frente.siguiente
            self.frente.siguiente = aux
        else:
            anterior = self.__get_nodo(posicion - 1)
            aux.siguiente = anterior.siguiente
            anterior.siguiente = aux

        self.tamanio += 1

    def localiza(self, valor, start=None, stop=None) -> int:
        """
        Devuelve la posicion de la priera aparición de "elemento" en la lista.
        Lanza exepción ValueError si elm elemento no está en la lista
        """
        if start == None:
            start = 0
        elif start < 0:
            start = len(self) + start
            if start < 0:
                start = 0
        elif start > 0:
            start = len(self)

        if stop == None:
            stop = len(self)
        elif stop < 0:
            stop = len(self) + stop
        elif stop > len(self):
            stop = len(self)

        posicion = start
        if posicion < stop:
            actual = self.__get_nodo(posicion)
            while posicion < stop:
                if actual.data == valor:
                    break
                else:
                    actual = actual.siguiente
                    posicion += 1
            else:
                raise self.ELEMENTO_NO_ENCONTRADO

        else:
            raise self.ELEMENTO_NO_ENCONTRADO

        return posicion

    def recupera(self, posicion):
        """
        Devuelve el elemento que está en la posición "posicion"
        Lanza "IndexError" si esa posicion no existe en la lista
        """
        return self.__get_nodo(posicion).data

    def suprime(self, posicion):
        """
        Elimina el elemento de la posición "posicion"
        Todas las posiciones posteriores a "posicion" son corridas a la
        izquierda 1 casillero
        """
        if posicion < 0:
            posicion = len(self) + posicion

        if posicion == 0:
            anterior = self.frente
        elif (posicion > 0) and (posicion < len(self)):
            anterior = self.__get_nodo(posicion - 1)
        else:
            raise self.POSICION_NO_VALIDA
        anterior.siguiente = anterior.siguiente.siguiente
        self.tamanio -= 1

    def modifica(self, posicion, valor):
        """ Modifica el valor de un elemento"""
        self.__get_nodo(posicion).data = valor

    def copy(self):
        """ Devuelve una copia de la lista"""
        copia = Lista()
        for elemento in self:
            copia.insert(elemento)
        return copia

    def reverse(self):
        """ Devuelve una copia de la lista en orden inverso"""
        nueva_lista = Lista()
        for elemento in self:
            nueva_lista.insert(elemento, 0)
        return nueva_lista

    def __repr__(self) -> str:
        strElementos = ''
        if len(self) > 0:
            for elemento in self:
                strElementos += repr(elemento) + ', '
            strElementos = strElementos[0:-2]

        representacion = '{self.__class__.__name__}({strElementos})'.format(
            self=self, strElementos=strElementos)
        return representacion

    def __regla_slice(self, posicion: slice) -> (int, int, int):
        paso = 1
        inicio = posicion.start
        fin = posicion.stop
        if posicion.step:
            if type(posicion.step) == int and posicion.step > 0:
                paso = posicion.step
            else:
                raise ValueError('"step" debe ser de tipo "int"')

        if posicion.start == None:
            inicio = 0
        elif posicion.start < 0:
            inicio = len(self) + posicion.start
            if inicio < 0:
                inicio = 0
        elif inicio > len(self):
            inicio = len(self)

        if posicion.stop == None:
            fin = len(self)
        elif posicion.stop < 0:
            fin = len(self) + posicion.stop
            if fin < 0:
                fin = 0
        elif posicion.stop > len(self):
            fin = len(self)

        return (inicio, paso, fin)

    def __getitem__(self, posicion):
        """x.__getitem__(y) <==> x[y]"""
        if type(posicion) == slice:
            (inicio, paso, fin) = self.__regla_slice(posicion)

            sublista = Lista()
            i = inicio
            if i < fin:
                actual = self.__get_nodo(i)
                while i < fin:
                    sublista.insert(actual.data)
                    actual = actual.siguiente
                    i += paso
            return sublista

        elif type(posicion) == int:
            if posicion < 0:
                posicion = len(self) + posicion
            return self.recupera(posicion)
        else:
            raise TypeError(
                'el indice debe ser "int" o "slice", no %s' % str(type(posicion)))

    def __setitem__(self, posicion, valor):
        if type(posicion) == slice:
            (inicio, paso, fin) = self.__regla_slice(posicion)

            i = inicio
            if i < fin:
                actual = self.__get_nodo(i)
                while i < fin:
                    actual.data = valor
                    actual = actual.siguiente
                    i += paso

        elif type(posicion) == int:
            self.modifica(posicion, valor)
        else:
            raise TypeError(
                'el indice debe ser "int" o "slice", no %s' % type(posicion))

    def __delitem__(self, posicion):
        """Delete self[key]."""
        if type(posicion) == int:
            self.suprime(posicion)
        elif type(posicion) == slice:
            (inicio, paso, fin) = self.__regla_slice(posicion)

            a_eliminar = Lista()
            i = inicio
            while i < fin:
                a_eliminar.append(i)
                i += paso
            a_eliminar.sort(reverse=True)
            for posicion in a_eliminar:
                self.suprime(posicion)
        else:
            raise TypeError(
                'el indice debe ser "int" o "slice", no %s' % type(posicion))

    def __add__(self, otra):
        """Return self+value"""
        if type(otra) == type(self):
            suma = self.copy()
            for elemento in otra:
                suma.insert(elemento)
            return suma
        else:
            raise TypeError('No se pueden sumar %s y %s' %
                            (type(self), type(otra)))

    def __contains__(self, valor):
        """Return key in self."""
        retorno = False

        for elemento in self:
            if elemento == valor:
                retorno = True
                break

        return retorno

    def __eq__(self, otra):
        """Return self==value."""
        es_igual = False
        if (type(otra) == type(self)) and (len(self) == len(otra)):
            es_igual = True
            for i in range(0, len(self)):
                if self[i] != otra[i]:
                    es_igual = False
                    break

        return es_igual

    def __gt__(self, otra):
        """Return self>value."""
        es_mayor = False
        if (type(otra) == type(self)) and (len(self) > len(otra)):
            es_mayor = True
            for i in range(0, len(otra)):
                if self[i] != otra[i]:
                    es_mayor = False
                    break
        return es_mayor

    def __ge__(self, otra):
        """Return self>=value."""
        return (self.__gt__(otra) or self.__eq__(otra))

    def __iadd__(self, otra):
        """Implement self+=value."""
        if (type(otra) == type(self)):
            for elemento in otra:
                self.insert(elemento)
        else:
            raise TypeError('Solo se puede sumar a otro %s' % (type(self)))
        return self

    def __imul__(self, entero):
        """Implement self*=value."""
        return self.__mul__(entero)

    def __le__(self, otra):
        """Return self<=value."""
        return otra > self

    def __mul__(self, entero):
        """Return self*value."""
        if type(entero) != int:
            raise TypeError('La Lista solo se puede multiplicar por un entero')
        else:
            aux = Lista()
            for i in range(0, entero):
                aux += self.copy()
        return aux

    def __ne__(self, otra):
        """Return self!=value."""
        return not (self == otra)

    def __rmul__(self, entero):
        """Return entero*self."""
        return self * entero

    def append(self, elemento):
        """Append object to the end of the list."""
        return self.insert(elemento)

    def clear(self):
        """Remove all items from list."""
        self.__init__()

    def count(self, valor):
        """Return number of occurrences of value."""
        contador = 0
        for elemento in self:
            if elemento == valor:
                contador += 1

        return contador

    def extend(self, objeto_iterable):
        """Extend list by appending elements from the iterable."""
        for elemento in objeto_iterable:
            self.insert(elemento)

    def index(self, valor, start=None, stop=None):
        """
        Return first index of value.
        Raises ValueError if the value is not present.
        """
        return self.localiza(valor, start, stop)

    # ITERATOR
    def __iter__(self):
        self._iter_actual = self.frente
        return self

    def __next__(self):
        if self._iter_actual.siguiente == None:
            raise StopIteration
        else:
            self._iter_actual = self._iter_actual.siguiente
            return self._iter_actual.data

    def pop(self, index=-1):
        """
        Remove and return item at index (default last).
        Raises IndexError if list is empty or index is out of range.
        """
        if index < 0:
            index = index + len(self)

        elemento = self.recupera(index)
        self.suprime(index)
        return elemento

    def remove(self, valor):
        """
        Elimina la primer ocurrencia de "valor"
        Lanza ValueError si el valor no se encuentra en la lista
        """
        anterior = self.frente
        actual = anterior.siguiente

        if len(self) == 0:
            raise self.ELEMENTO_NO_ENCONTRADO

        while True:
            if actual.data == valor:
                if actual == self.__ultimo__:
                    self.__ultimo__ = anterior
                anterior.siguiente = anterior.siguiente.siguiente
                self.tamanio -= 1
                break
            elif actual.siguiente == None:
                raise self.ELEMENTO_NO_ENCONTRADO
            else:
                anterior = actual
                actual = actual.siguiente

    def sort(self, reverse=False):
        """
        Ordena la lista en orden ascendente o descentente si "reverse == True"
        """

        def intercambiar(este, este_otro):
            return (este_otro, este)

        if len(self) > 1:
            hubo_cambios = True
            while hubo_cambios:
                hubo_cambios = False
                i = 1
                actual = self.frente.siguiente
                siguiente = actual.siguiente
                while i < len(self):
                    condicion = (reverse and (actual.data < siguiente.data))
                    condicion = condicion or (not reverse and (actual.data > siguiente.data))

                    if condicion:
                        (actual.data, siguiente.data) = intercambiar(actual.data, siguiente.data)
                        hubo_cambios = True

                    i += 1
                    actual = siguiente
                    siguiente = siguiente.siguiente

    def sort_func(self, func):
        """
        Ordena la lista de acuerdo a una funcion "func(actual, siguiente)"
        func(actual, siguiente) -> True si actual > siguiente
        func(actual, siguiente) -> False si actual <= siguiente
        """

        def intercambiar(este, este_otro):
            return (este_otro, este)

        if len(self) > 1:
            hubo_cambios = True
            while hubo_cambios:
                hubo_cambios = False
                i = 1
                actual = self.frente.siguiente
                siguiente = actual.siguiente
                while i < len(self):

                    if func(actual.data, siguiente.data):
                        (actual.data, siguiente.data) = intercambiar(actual.data, siguiente.data)
                        hubo_cambios = True

                    i += 1
                    actual = siguiente
                    siguiente = siguiente.siguiente