#ifndef NODOLISTADOBLEENLAZADA_H
#define NODOLISTADOBLEENLAZADA_H
#include <string>
#include <iostream>

using namespace std;

class NodoListaDobleEnlazada
{
    private:
        string nombre;
        int edad;
        int index;
        NodoListaDobleEnlazada *NextD;
        NodoListaDobleEnlazada *PrevD;
    public:
        NodoListaDobleEnlazada();
        NodoListaDobleEnlazada(string nombre_, int edad_, int index_, NodoListaDobleEnlazada *NextD_, NodoListaDobleEnlazada *PrevD_);
        //gets
        string getNombre();
        int getEdad();
        int getIndex();
        NodoListaDobleEnlazada *getNextD();
        NodoListaDobleEnlazada *getPrevD();
        //sets
        void setNombre(string nombre_);
        void setEdad(int edad_);
        void setIndex(int index_);
        void setNextD(NodoListaDobleEnlazada *NextD_);
        void setPrevD(NodoListaDobleEnlazada *PrevD_);
};

#endif // NODOLISTADOBLEENLAZADA_H
