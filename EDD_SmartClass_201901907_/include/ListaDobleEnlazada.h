#ifndef LISTADOBLEENLAZADA_H
#define LISTADOBLEENLAZADA_H
#include "NodoListaDobleEnlazada.h"

class ListaDobleEnlazada
{
    public:
        ListaDobleEnlazada();
        int getSize();
        void getList();
        bool isEmpty();
        void PrintList();
        void Eliminar(string id);
        void Modificar(string id);
        void insertar(string id, string mes, string dia, string hora, string carnet, string nombre, string descripcion, string materia, string fecha, string estado);
        void deleteValue (string id);
        void buscarPos(string pos);
        void buscar2(string pos);
        void Grafico();

    private:
        NodoListaDobleEnlazada *First;
        NodoListaDobleEnlazada *Last;
};

#endif // LISTADOBLEENLAZADA_H
