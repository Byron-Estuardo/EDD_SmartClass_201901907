from math import sqrt, trunc
from lista import Lista


class Item:
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor

    def __eq__(self, value):
        """
        return self == value
        """
        if type(value) == Item:
            return self.clave == value.clave
        else:
            return self.clave == value

    def __str__(self):
        return f"{repr(self.clave)}: {repr(self.valor)}"

    def __repr__(self):
        return Item(repr(self.clave), repr(self.valor))


class TablaHash:
    def __init__(self, tamanio=20):
        self.__tamanio_tabla = tamanio
        self.__tamanio_tabla = self.__siguiente_primo(self.__tamanio_tabla)
        self.__tabla = []
        self.__cantidad_items = 0
        for i in range(0, self.__tamanio_tabla):
            self.__tabla.append(Lista())

    def insertar(self, clave, valor):
        """
        Inserta un nuevo par (clave, valor) en el diccionario,
        si la clave ya existe lanza KeyError
        """
        valor_hash = self.__hash(clave)
        if self.__existe_clave(clave):
            raise KeyError(f'La clave "{clave}" ya existe')
        else:
            self.__insert(valor_hash, Item(clave, valor))

    def eliminar(self, clave):
        """
        Elimina un par (clave, valor) del diccionario
        """
        valor_hash = self.__hash(clave)
        try:
            self.__delete(valor_hash, clave)
        except ValueError:
            raise KeyError('La clave no se encuentra en el diccionario')

    def buscar(self, clave):
        """
        Busca y devuelve un valor del diccionario,
        si no se encuentra la clave se lanza una exepción KeyError
        """
        item = self.__buscar_item(clave)
        if item is None:
            raise KeyError(f'El elemento "{clave}" no se encuentra en el diccionario')
        else:
            return item.valor

    def obtener(self, clave):
        """
        Busca y devuelve un valor del diccionario o "None"
        """
        item = self.__buscar_item(clave)

        if item is None:
            return None
        else:
            return item.valor

    def actualizar(self, clave, nuevo_valor):
        """
        Actualiza el valor de una clave, si no se encuentra la clave la crea
        """

        item = self.__buscar_item(clave)
        if item is None:
            valor_hash = self.__hash(clave)
            self.__insert(valor_hash, Item(clave, nuevo_valor))
        else:
            item.valor = nuevo_valor

    def __hash(self, clave):
        """Funcion hash"""
        if type(clave) == str:
            ponderacion = 53
            suma = 0
            i = 1
            for letra in clave:
                suma += ord(letra) * ponderacion ** i
                i += 1
            valor_hash = suma % self.__tamanio_tabla
        elif type(clave) == int:
            valor_hash = clave % self.__tamanio_tabla
        else:
            raise ValueError('La clave debe ser "int" o "str"')

        return valor_hash

    def __siguiente_primo(self, tamanio):
        """
        Devuelve el primo siguiente al tamanio necesario de tabla
        """

        def es_primo(numero):
            if numero <= 1:
                b_es_primo = False
            elif numero == 2:
                b_es_primo = True
            elif numero % 2 == 0:
                b_es_primo = False
            else:
                b_es_primo = True

                limite = trunc(sqrt(numero))
                for cociente in range(3, limite + 1, 2):
                    if (numero % cociente == 0):
                        b_es_primo = False
            return b_es_primo

        while True:
            if es_primo(tamanio):
                return tamanio
            else:
                tamanio += 1

    def __getitem__(self, clave):
        """
        self[clave]
        """
        return self.buscar(clave)

    def __setitem__(self, clave, valor):
        """
        self[clave] = valor
        """
        return self.actualizar(clave, valor)

    def __delitem__(self, clave):
        """
        del self[clave]
        """
        return self.eliminar(clave)

    def items(self):
        """
        Iterable de todos los pares
        """
        for lista in self.__tabla:
            for item in lista:
                yield (item.clave, item.valor)

    def __len__(self):
        cantidad = 0
        for lista in self.__tabla:
            cantidad += len(lista)

    def __insert(self, valor_hash, item):
        """
        Metodo bajo nivel insercion item
        """
        self.__tabla[valor_hash].insert(item)
        self.__cantidad_items += 1

        factor = self.__cantidad_items / self.__tamanio_tabla
        if factor >= 0.75:
            self.__rehashing()

    def __rehashing(self):
        """
        Crea una tabla nueva del doble de tamaño
        """
        tabla_aux = TablaHash(self.__tamanio_tabla * 2)
        for clave, valor in self.items():
            tabla_aux.insertar(clave, valor)
        self.__tabla = tabla_aux.__tabla
        self.__tamanio_tabla = tabla_aux.__tamanio_tabla

    def __delete(self, valor_hash, clave):
        """
        Metodo bajo nivel de eliminacion de item
        """
        self.__tabla[valor_hash].remove(clave)
        self.__cantidad_items -= 1

    def __buscar_item(self, clave):
        """
        devuelve "Item" si una clave se encuentra en la tabla
        o "None" si no se encuentra
        """
        item = None
        valor_hash = self.__hash(clave)
        for elemento in self.__tabla[valor_hash]:
            if elemento.clave == clave:
                item = elemento
                break
        return item

    def __existe_clave(self, clave):
        """
        Devuelve True si la clave se encuentra en la tabla
        """
        existe = True
        item = self.__buscar_item(clave)
        if item is None:
            existe = False

        return existe


class TablaHashCerrada:
    """
    TDA para tabla hash con direccionamiento cerrado
    ------------------------------------------------
    Las posiciones con elementos borrados son Item() con clave None.
    Exploracion lineal.
    """

    def __init__(self, tamanio=20):
        self.__tamanio_tabla = tamanio
        self.__tamanio_tabla = self.__siguiente_primo(self.__tamanio_tabla)
        self.__tabla = []
        self.__cantidad_items = 0
        for i in range(0, self.__tamanio_tabla):
            self.__tabla.append(None)

    def insertar(self, clave, valor):
        """
        Inserta un nuevo par (clave, valor) en el diccionario,
        si la clave ya existe lanza KeyError
        """
        valor_hash = self.__hash(clave)
        if self.__existe_clave(clave):
            raise KeyError(f'La clave "{clave}" ya existe')
        else:
            self.__insert(valor_hash, Item(clave, valor))

    def eliminar(self, clave):
        """
        Elimina un par (clave, valor) del diccionario
        """
        valor_hash = self.__hash(clave)
        try:
            self.__delete(valor_hash, clave)
        except KeyError:
            raise KeyError(f'La clave "{clave}" no se encuentra en el diccionario')

    def buscar(self, clave):
        """
        Busca y devuelve un valor del diccionario, si no se encuentra la clave
        se lanza una excepción KeyError
        """
        item = self.__buscar_item(clave)
        if item is None:
            raise KeyError(f'La clave "{clave}" no se encuentra en el diccionario')
        else:
            return item.valor

    def obtener(self, clave):
        """
        Busca y devuelve un valor del diccionario o "None"
        """
        item = self.__buscar_item(clave)

        if item is None:
            return None
        else:
            return item.valor

    def actualizar(self, clave, nuevo_valor):
        """
        Actualiza el valor de una clave, si no se encuentra la clave la crea
        """

        item = self.__buscar_item(clave)
        if item is None:
            valor_hash = self.__hash(clave)
            self.__insert(valor_hash, Item(clave, nuevo_valor))
        else:
            item.valor = nuevo_valor

    def __hash(self, clave):
        """Funcion hash"""
        if type(clave) == str:
            ponderacion = 53
            suma = 0
            i = 1
            for letra in clave:
                suma += ord(letra) * ponderacion ** i
                i += 1
            valor_hash = suma % self.__tamanio_tabla
        elif type(clave) == int:
            valor_hash = clave % self.__tamanio_tabla
        else:
            raise ValueError('La clave debe ser "int" o "str"')

        return valor_hash

    def __siguiente_primo(self, tamanio):
        """
        Devuelve el primo siguiente al tamanio necesario de tabla
        """

        def es_primo(numero):
            if numero <= 1:
                b_es_primo = False
            elif numero == 2:
                b_es_primo = True
            elif numero % 2 == 0:
                b_es_primo = False
            else:
                b_es_primo = True

                limite = trunc(sqrt(numero))
                for cociente in range(3, limite + 1, 2):
                    if (numero % cociente == 0):
                        b_es_primo = False
            return b_es_primo

        while True:
            if es_primo(tamanio):
                return tamanio
            else:
                tamanio += 1

    def __getitem__(self, clave):
        """
        self[clave]
        """
        return self.buscar(clave)

    def __setitem__(self, clave, valor):
        """
        self[clave] = valor
        """
        return self.actualizar(clave, valor)

    def __delitem__(self, clave):
        """
        del self[clave]
        """
        return self.eliminar(clave)

    def items(self):
        """
        Iterable de todos los pares
        """
        for item in self.__tabla:
            if (not item) or (not item.clave):
                continue
            yield (item.clave, item.valor)

    def __len__(self):
        return self.__cantidad_items

    def __insert(self, valor_hash, item):
        """
        Metodo bajo nivel insercion item
        (No verifica la existencia de la clave, solo inserta)
        Resolucion de colisiones: Lineal
        """

        while True:
            if (self.__tabla[valor_hash] is None) or (self.__tabla[valor_hash].clave is None):
                self.__tabla[valor_hash] = item
                self.__cantidad_items += 1
                break

            valor_hash += 1
            valor_hash %= self.__tamanio_tabla

        factor = self.__cantidad_items / self.__tamanio_tabla
        if factor >= 0.8:
            self.__rehashing()

    def __rehashing(self):
        """
        Crea una tabla nueva del doble de tamaño
        """
        tabla_aux = TablaHashCerrada(self.__tamanio_tabla * 2)
        for clave, valor in self.items():
            tabla_aux.insertar(clave, valor)
        self.__tabla = tabla_aux.__tabla
        self.__tamanio_tabla = tabla_aux.__tamanio_tabla

    def __delete(self, valor_hash, clave):
        """
        Metodo bajo nivel de eliminacion de item.
        """
        item = self.__buscar_item(clave)
        if item:
            item.clave = None
            self.__cantidad_items -= 1
        else:
            raise KeyError(f'El elemento con clave {clave} no existe')

    def __buscar_item(self, clave):
        """
        devuelve "Item" si una clave se encuentra en la tabla
        o "None" si no se encuentra
        """
        item = None
        valor_hash = self.__hash(clave)

        if self.__tabla[valor_hash] and (self.__tabla[valor_hash].clave == clave):
            return self.__tabla[valor_hash]
        else:
            valor_hash += 1
            valor_hash %= self.__tamanio_tabla

            while (not item) and self.__tabla[valor_hash]:
                if self.__tabla[valor_hash].clave == clave:
                    item = self.__tabla[valor_hash]

                valor_hash += 1
                valor_hash %= self.__tamanio_tabla

        return item

    def __existe_clave(self, clave):
        """
        Devuelve True si la clave se encuentra en la tabla
        """
        existe = True
        item = self.__buscar_item(clave)
        if item is None:
            existe = False

        return existe