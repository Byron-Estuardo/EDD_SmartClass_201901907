#include "Colaa.h"
#include <iostream>
#include <fstream>

using namespace std;

void Colaa::Inicializar(){
    this->Primero = NULL;
    this->Fin = NULL;
}

bool Colaa::Vacia(){
    if(this->Primero == NULL && this->Fin == NULL){
        return true;
    }
    else{
        return false;
    }
}

void Colaa::Encolar(string Tipo_, string Campo_){
    Nodo *temporal = new Nodo;
    temporal->Campo = Campo_;
    temporal->Tipo = Tipo_;
    temporal->siguiente = NULL;
    temporal->anterior = NULL;
    if(Vacia()){
        this->Primero = temporal;
        this->Fin = this->Primero;
    }
    else{
        this->Fin->siguiente = temporal;
        temporal->anterior = this->Fin;
        this->Fin = temporal;
    }
}

void Colaa::Desencolar(){
    Nodo *auxiliar;
    auxiliar = Primero;
    Primero = Primero->siguiente;
    delete auxiliar;
}

int Colaa::Tamano(){
    int contador = 0;
    Nodo *auxiliar;
    auxiliar = Primero;
    while(auxiliar != NULL){
        contador++;
        auxiliar = auxiliar->siguiente;
    }
    return contador;
}

void Colaa::grafico()
{
    int contador = 0;
    ofstream archivo("errores.dot");
    archivo << "digraph G {\n";
    archivo << "rankdir=LR;\n";
    archivo << "node[shape = record];\n ";
    Nodo *aux = new Nodo();
    aux = Primero;
    if (this->Primero != NULL)
    {
        do
        {
            int contador2 = contador + 1;
            string str1 = std::to_string(contador);
            string str2 = std::to_string(contador + 1);
            archivo << "nodo" + str1 << "[label=\" Tipo: " + Primero->siguiente->Tipo+ "\n|Descripcion: " + Primero->siguiente->Campo + "\" ]";

            if (aux->anterior == Primero)
            {
                archivo << "\n nodo" + str1 + "-> nodo0\n";
            }
            else
            {
                archivo << "\n nodo" + str1 + "->" + "nodo" + str2 + "\n";
            }
            contador++;
            aux = aux->anterior;
        } while (aux != Fin);
        archivo << "}\n";
        archivo.close();
        string ej= "dot -Tpng errores.dot -o errores.png";
        char const *ejecutar = ej.c_str();
        system(ejecutar);
    }
    else
    {
        cout << "La Cola esta vacia !!!\n";
    }

}

