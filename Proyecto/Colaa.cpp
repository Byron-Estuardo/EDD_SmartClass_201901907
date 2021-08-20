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
    if(Vacia()){
        this->Primero = temporal;
        this->Fin = temporal;
    }
    else{
        this->Fin->siguiente = temporal;
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

    /*
    int contador = 0;
    Nodo *auxiliar;
    auxiliar = Primero;
    while(auxiliar != NULL){
        contador++;
        auxiliar = auxiliar->siguiente;
    }
    return contador;
    */
    int contador = 0;
    ofstream archivo("errores.dot");
    archivo << "digraph G {\n";
    archivo << "rankdir=LR;\n";
    archivo << "node[shape = record];\n ";
    Nodo *temporal = new Nodo();
    temporal = Primero;
    while(temporal != NULL){
        cout<<"Entro??"<<endl;
        int contador2 = contador + 1;
        cout<<contador2<<endl;
        cout<<contador<<endl;
        string str1 = std::to_string(contador);
        string str2 = std::to_string(contador2);
        cout<<str2<<endl;
        cout<<str1<<endl;
        cout<<temporal->siguiente->Campo<<endl;
        cout<<temporal->siguiente->Tipo<<endl;

        archivo << "nodo" + str1 << "[label=\"Tipo: " + temporal->siguiente->Tipo + "\n|Descripcion: " + temporal->siguiente->Campo + "\" ]";

        if (temporal != NULL)
        {
            cout<<"entro if primero"<<endl;
            archivo << "\n nodo" + str1 + "->" + "nodo" + str2 + "\n";
        }
        else
        {
            cout<<"entro else"<<endl;
            archivo << "nodo" + str1 + "\n";
        }

        contador++;
        temporal = temporal->siguiente;
        cout<<"Salida while "<<endl;
        cout<<temporal->Campo << " \n"<<endl;
    }
    archivo << "}\n";
    archivo.close();
    string ej= "dot -Tpng errores.dot -o errores.png";
    char const *ejecutar = ej.c_str();
    system(ejecutar);
}

