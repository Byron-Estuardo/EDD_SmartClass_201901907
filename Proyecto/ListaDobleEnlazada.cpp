#include "ListaDobleEnlazada.h"

void Lista::Inicializar(){
    Cabeza = NULL;
    Cola = NULL;
}

bool Lista::Vacia{
    if(Cabeza == NULL && Cola == NULL){
        return true;
    }
    else{
        return false;
    }
}

int Lista::Tamano(){
    int contador = 0;
    Nodo *auxiliar;
    auxiliar = Cabeza;
    while(auxiliar != NULL){
        contador++;
        auxiliar = auxiliar->sig;
    }
    return contador;
}

void Lista::Mostrar(){
    Nodo *auxiliar;
    auxiliar = Cabeza;
    while(auxiliar != NULL){
        count<<auxiliar->dato<<endl;
        auxiliar = auxiliar->sig;
    }
}

void Lista::InsertIni(int dato){
    Nodo *temp = new Nodo;
    temp->dato = dato;
    temp->sig = NULL;
    temp->ant = NULL;

    if(Vacia()){
        Cabeza = temp;
        Cola = temp;
    }
    else{
        temp->sig = Cabeza;
        Cabeza->ant = temp;
        Cabeza = temp;
    }
}

void Lista::InsertFin(int dato){
    Nodo *temp = new Nodo;
    temp->dato = dato;
    temp->sig = NULL;
    temp->ant = NULL;

    if(Vacia()){
        Cabeza = temp;
        Cola = temp;
    }
    else{
        Cola->sig = temp;
        temp->ant = Cola;
        Cola = temp;
    }
}


void Lista::InsertPosEs(int dato, int posicion){
    Nodo *temp = new Nodo;
    temp->dato = dato;
    temp->sig = NULL;
    temp->ant = NULL;

    if(Vacia()){
        Cabeza = temp;
        Cola = temp;
    }
    else{
        if(posicion == 1){
            InsertIni(dato);
        }
        else if(posicion == (Tamano() + 1)){
            InsertFin(dato);
        }
        else if(posicion > 1 && posicion < (Tamano() + 1)){
            Nodo *auxiliar;
            auxiliar = Cabeza;
            for(int i=1; i<posicion; i++){
                auxiliar = auxiliar->sig;
            }
            auxiliar->ant->sig = temp;
            temp->sig = auxiliar;
            temp->ant = auxiliar->ant;
            auxiliar->ant = temp;
        }
        else{
            count<<"Error Prraaaaaa"<<endl;
        }
    }

}

void Lista::Eliminar(int posicion){
    Nodo *auxiliar;
    if(posicion == 1){
        auxiliar = Cabeza;
        Cabeza = Cabeza->sig;
        delete(auxiliar);
    }
    else if(posicion == Tamano()){
        auxiliar = Cola;
        Cola = Cola->ant;
        delete(auxiliar);
    }
    else if(posicion > 1 || posicion < Tamano()){
        auxiliar = Cabeza;
        for(int i=1; i<posicion; i++){
            auxiliar = auxiliar->sig;
        }
        auxiliar->ant->sig = auxiliar->sig;
        Cola->ant = auxiliar->ant;
        delete(auxiliar)
    }
    else{
        count<<"Error"<<endl
    }
}

void Lista::Anular(){
    Nodo *auxiliar;
    while(h != NULL){
        auxiliar = Cabeza;
        Cabeza = Cabeza->sig;
        delete(auxiliar);
    }
}

int Lista::BuscarPorPos(int posicion){
    Nodo *auxiliar;
    if(posicion >= 1 || posicion <= Tamano()){
        auxiliar = Cabeza;
        for(int i=1; i<posicion; i++){
            auxiliar = auxiliar->sig;
        }
        return aux->dato;
    }
    return -1;
}

int Lista::BuscarPorPos(int dato){
    int contador = 1;
    Nodo *auxiliar;
    auxiliar = Cabeza;
    while(auxiliar != NULL){
        if(auxiliar->dato == dato){
            return contador;
        }
        contador++;
        auxiliar = auxiliar->sig;
    }
    return -1;
}

