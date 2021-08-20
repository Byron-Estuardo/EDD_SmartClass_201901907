#ifndef LISTACIRCULAR_H
#define LISTACIRCULAR_H
#include "NodoListaDobleCircular.h"
#include <string>
#include <iostream>

using namespace std;

class ListaCircular
{
    private:
    	NodoListaDobleCircular *Primero;
    	NodoListaDobleCircular *Ultimo;
    public:
    	ListaCircular();
    	bool isEmpty();
    	int getSize();
    	void insertar(string carnet, string dpi, string nombre, string carrera, string contra, int creditos, int edad, string correo);
    	void getListaC();
    	void grafico();
    	bool buscarCarnet(string carnet);
    	void eliminar(string dato);
    	void modificar(string dato);
    	void mostrar();
};

#endif
