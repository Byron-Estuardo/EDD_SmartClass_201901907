#include "NodoMatriz.h"

NodoMatriz::NodoMatriz(){
    this->id = "";
    this->mes = "";
    this->dia = "";
    this->hora= "";
    this->carnet = "";
    this->nombre = "";
    this->descripcion = "";
    this->materia = "";
    this->fecha = "";
    this->estado = "";
}

NodoMatriz::NodoMatriz(string id_,string mes_,string dia_,string hora_, string carnet_, string nombre_, string descripcion_, string materia_, string fecha_, string estado_)
{
    this->id = id_;
    this->mes = mes_;
    this->dia = dia_;
    this->hora = hora_;
    this->carnet = carnet_;
    this->nombre = nombre_;
    this->descripcion = descripcion_;
    this->materia = materia_;
    this->fecha = fecha_;
    this->estado = estado_;
}

string NodoMatriz::getId()
{
    return this->id;
}

string NodoMatriz::getMes(){
    return this->mes;
}

string NodoMatriz::getDia(){
    return this->dia;
}

string NodoMatriz::getHora(){
    return this->hora;
}

string NodoMatriz::getCarnet()
{
    return this->carnet;
}

string NodoMatriz::getNombre(){
    return this->nombre;
}

string NodoMatriz::getDescripcion(){
    return this->descripcion;
}

string NodoMatriz::getMateria(){
    return this->materia;
}

string NodoMatriz::getFecha(){
    return this->fecha;
}

string NodoMatriz::getEstado(){
    return this->estado;
}


void NodoMatriz::setId(string id_)
{
    this->id = id_;
}

void NodoMatriz::setMes(string mes_){
    this->id = mes_;
}

void NodoMatriz::setDia(string dia_){
    this->dia = dia_;
}

void NodoMatriz::setHora(string hora_){
    this->hora = hora_;
}

void NodoMatriz::setCarnet(string carnet_){
    this->carnet = carnet_;
}

void NodoMatriz::setNombre(string nombre_){
    this->nombre = nombre_;
}

void NodoMatriz::setDescripcion(string descripcion_){
    this->descripcion = descripcion_;
}

void NodoMatriz::setMateria(string materia_){
    this->materia = materia_;
}

void NodoMatriz::setFecha(string fecha_){
    this->fecha = fecha_;
}

void NodoMatriz::setEstado(string estado_){
    this->estado = estado_;
}


