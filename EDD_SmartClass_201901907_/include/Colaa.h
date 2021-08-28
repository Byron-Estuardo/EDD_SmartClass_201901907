#ifndef COLAA_H
#define COLAA_H
#include <iostream>

using namespace std;

class Nodo
{
    Nodo *siguiente;
    Nodo *anterior;
    string Tipo;
    string Campo;
    friend class Colaa;
};

class Colaa
{
  private:
    Nodo *Primero;
    Nodo *Fin;
  public:
      void Inicializar();
      bool Vacia();
      void Encolar(string Tipo_, string Campo_);
      void Desencolar();
      int Tamano();
	  void grafico();
};

#endif // COLAA_H

