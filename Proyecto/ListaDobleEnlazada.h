#ifndef LDE_H_INCLUDED
#define LDE_H_INCLUDED
#include <iostream>

using namespace std;

class Nodo
{
    Nodo *sig;
    Nodo *ant;
    int dato;
    friend class Lista;
};

class Lista
{
    Nodo *Cabeza;
    Nodo *Cola;
    public:
        void Inicializar();
        bool Vacia();
        int Tamano();
        void Mostrar();
        void InsertIni(int dato);
        void InsertFin(int dato);
        void InsertPosEs(int dato, int posicion);
        void Eliminar(int posicion);
        void Anular();
        int BuscarPorPos(int posicion);
        int BuscarPorDato(int dato);
};

#endif // LDE_H_INCLUDED
