#include "ListaDobleEnlazada.h"
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <iomanip>
#include<string>
#include <sstream>
using namespace std;

ListaDobleEnlazada::ListaDobleEnlazada(){
    this->First = NULL;
    this->Last = NULL;
}

int ListaDobleEnlazada::getSize(){
    NodoListaDobleEnlazada *aux = First;
    int contador = 0;
    while(aux != NULL){
        contador++;
        aux = aux->getNextD();
    }
    delete aux;
    return contador;
}

bool ListaDobleEnlazada::isEmpty(){
    return this->First == NULL;
}

void ListaDobleEnlazada::PrintList(){
    NodoListaDobleEnlazada *aux = First;
    while(aux != NULL){
        cout<<"Index: "<<aux->getId()<<endl;
        cout<<"Mes: "<<aux->getMes()<<endl;
        cout<<"Dia: "<<aux->getDia()<<endl;
        cout<<"Hora: "<<aux->getHora()<<endl;
        cout<<"Carnet: "<<aux->getCarnet()<<endl;
        cout<<"Nombre: "<<aux->getNombre()<<endl;
        cout<<"Descripcion: "<<aux->getDescripcion()<<endl;
        cout<<"Materia: "<<aux->getMateria()<<endl;
        cout<<"Fecha: "<<aux->getFecha()<<endl;
        cout<<"Estado: "<<aux->getEstado()<<endl;
        aux = aux->getNextD();
    }
    delete aux;
}

void ListaDobleEnlazada::getPersonRow(string id, string mes, string dia, string hora, string carnet, string nombre, string descripcion, string materia, string fecha, string estado){
    /*
    NodoListaDobleEnlazada *aux = First;
    while(aux != NULL){
        if(aux->getId() == (year*12+mes)){
            cout<<aux->getNombre()<<endl;
            break;
        }
        aux = aux->getNextD();
    }
    delete aux;*/
}

void ListaDobleEnlazada::insertar(string id_, string mes_, string dia_, string hora_, string carnet_, string nombre_, string descripcion_, string materia_, string fecha_, string estado_)
{
    NodoListaDobleEnlazada *newNode = new NodoListaDobleEnlazada( id_, mes_, dia_, hora_, carnet_,  nombre_,  descripcion_,  materia_,  fecha_,  estado_, NULL, NULL);
    if(isEmpty()){
        this->First = newNode;
        this->Last = this->First;
    }
    else{
        this->Last->setNextD(newNode);
        newNode->setPrevD(this->Last);
        this->Last = newNode;
    }
}
