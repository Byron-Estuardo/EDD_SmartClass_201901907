#include "NodoListaDobleEnlazada.h"

NodoListaDobleEnlazada::NodoListaDobleEnlazada()
{
    NodoListaDobleEnlazada()
    {
        this->edad = 0;
        this->nombre = "";
        this->index = 0;
        this->NextD = NULL;
        this->PrevD = NULL;
    }
    NodoListaDobleEnlazada(string nombre_, int edad_, int index_, NodoListaDobleEnlazada *NextD_, NodoListaDobleEnlazada *PrevD_)
    {
        this->edad = edad_;
        this->nombre = nombre_;
        this->index = index_;
        this->NextD = NextD_;
        this->PrevD = PrevD_;
    }
    //gets
    string getNombre()
    {
        return this->nombre;
    }
    int getEdad()
    {
        return this->edad;
    }
    int getIndex()
    {
        return this->index;
    }
    NodoListaDobleEnlazada *getNextD()
    {
        return this->NextD;
    }
    NodoListaDobleEnlazada *getPrevD()
    {
        return this->PrevD;
    }
    //sets
    void setNombre(string nombre_)
    {
        this->nombre = nombre_;
    }
    void setEdad(int edad_)
    {
        this->edad = edad_;
    }
    void setIndex(int index_)
    {
        this->index = index_;
    }
    void setNextD(NodoListaDobleEnlazada *NextD_)
    {
        this->NextD = NextD_;
    }
    void setPrevD(NodoListaDobleEnlazada *PrevD_)
    {
        this->PrevD = PrevD_;
    }
}

