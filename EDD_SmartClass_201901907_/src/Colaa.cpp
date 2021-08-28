#include "Colaa.h"
#include <iostream>
#include <fstream>

using namespace std;

string Colaa::getCampo(Nodo *Nodo){
    return Nodo->Campo;
}

string Colaa::getTipo(Nodo *Nodo){
    return Nodo->Tipo;
}

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
    /*Nodo *auxiliar;
    auxiliar = Primero;
    Primero = Primero->siguiente;
    delete auxiliar;*/
    Nodo *auxiliar;
    auxiliar = Primero;
    if(Primero == Fin){
        Primero = NULL;
        Fin = NULL;
    }
    else{
        Primero = Primero->siguiente;
    }
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
    aux = this->Primero;
    while(this->Primero != NULL){
        Desencolar();
        int contador2 = contador + 1;
        string str1 = std::to_string(contador);
        string str2 = std::to_string(contador2);
        cout<<getTipo(aux)<<endl;
        cout<<getCampo(aux)<<endl;
        archivo << "nodo" + str1 << "[label=\" Tipo: " + getTipo(aux) + "\n|Descripcion: " + getCampo(aux) + "\" ]";
        if(this->Primero != NULL){
            archivo << "\nnodo0 -> nodo" + str2 + "\n";
            contador++;
        }
        else{
            archivo << "\nnodo" + str2 + "->" + "nodo" + str1 + "\n";
            contador++;
        }

    }
    archivo << "}\n";
    archivo.close();
    string ej= "dot -Tpng errores.dot -o errores.png";
    char const *ejecutar = ej.c_str();
    system(ejecutar);
}

